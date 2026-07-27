#!/usr/bin/env python3
"""Publish eligible managed Markdown documents to existing Confluence pages.

The tool never changes document status or enables publication. A document is
eligible only when its front matter contains:

    confluence:
      publish: true
      page_id: "123456"

Dry-run is the default. A live update requires both ``--live`` and
``--confirm-live UPDATE-CONFLUENCE``.

A document with an empty ``page_id`` can be created only when it has a numeric
``parent_page_id`` and the caller supplies ``--create-missing``. Existing pages
are always updated by ID.
"""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

from atlassian import Confluence
import markdown
import yaml

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from env_utils import load_workspace_env


LIVE_CONFIRMATION = "UPDATE-CONFLUENCE"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or update existing Confluence pages from managed Markdown documents."
    )
    parser.add_argument(
        "documents",
        nargs="+",
        type=Path,
        help="Managed Markdown documents to preview or publish.",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Perform updates. Without this flag the tool only previews.",
    )
    parser.add_argument(
        "--confirm-live",
        default="",
        metavar="TEXT",
        help=f"Required with --live; value must be {LIVE_CONFIRMATION!r}.",
    )
    parser.add_argument(
        "--create-missing",
        action="store_true",
        help="Allow documents without page_id to be created under parent_page_id.",
    )
    return parser.parse_args()


def load_document(path: Path) -> tuple[dict[str, Any], str]:
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT_DIR)
    except ValueError as exc:
        raise ValueError(f"Document must be inside the repository: {path}") from exc

    text = resolved.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing YAML front matter: {path}")

    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError(f"Invalid YAML front matter: {path}")

    required = {"id", "title", "type", "status", "owner", "updated", "confluence"}
    missing = sorted(required - metadata.keys())
    if missing:
        raise ValueError(f"Missing required metadata in {path}: {', '.join(missing)}")

    return metadata, match.group(2)


def validate_publication(
    metadata: dict[str, Any], path: Path, create_missing: bool
) -> dict[str, str]:
    confluence = metadata.get("confluence")
    if not isinstance(confluence, dict):
        raise ValueError(f"Invalid confluence metadata in {path}")
    if confluence.get("publish") is not True:
        raise ValueError(
            f"Publication is not approved for {metadata.get('id')} "
            "(confluence.publish must be true)."
        )

    page_id = str(confluence.get("page_id", "")).strip()
    parent_page_id = str(confluence.get("parent_page_id", "")).strip()
    space_key = str(confluence.get("space_key", "")).strip()
    title = str(confluence.get("title", metadata.get("title", ""))).strip()

    if not title:
        raise ValueError(f"Confluence title required for {metadata.get('id')}")
    if page_id:
        if not page_id.isdigit():
            raise ValueError(
                f"Numeric confluence.page_id required for {metadata.get('id')}"
            )
        return {
            "mode": "update",
            "page_id": page_id,
            "parent_page_id": parent_page_id,
            "space_key": space_key,
            "title": title,
        }

    if not create_missing:
        raise ValueError(
            f"{metadata.get('id')} has no page_id; use --create-missing to preview "
            "or create its configured child page."
        )
    if not parent_page_id.isdigit() or not space_key:
        raise ValueError(
            f"{metadata.get('id')} requires confluence.space_key and numeric "
            "confluence.parent_page_id for creation."
        )
    return {
        "mode": "create",
        "page_id": "",
        "parent_page_id": parent_page_id,
        "space_key": space_key,
        "title": title,
    }


def git_revision() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT_DIR,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_source_url(revision: str, path: Path) -> str | None:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=ROOT_DIR,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None

    remote = result.stdout.strip()
    match = re.match(r"(?:https://github\.com/|git@github\.com:)(.+?)(?:\.git)?$", remote)
    if not match:
        return None

    relative = path.resolve().relative_to(ROOT_DIR).as_posix()
    return f"https://github.com/{match.group(1)}/blob/{revision}/{relative}"


def markdown_to_storage(
    metadata: dict[str, Any], body: str, revision: str, source_url: str | None
) -> str:
    source = (
        f'<a href="{html.escape(source_url, quote=True)}">{html.escape(revision)}</a>'
        if source_url
        else html.escape(revision)
    )
    banner = (
        '<div class="generated-from-github">'
        f"<p><strong>Source document:</strong> {html.escape(str(metadata['id']))}<br />"
        f"<strong>Lifecycle status:</strong> {html.escape(str(metadata['status']))}<br />"
        f"<strong>Git revision:</strong> {source}<br />"
        f"<strong>Last updated:</strong> {html.escape(str(metadata['updated']))}</p>"
        "</div>"
    )
    rendered = markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="xhtml",
    )
    return banner + rendered


def confluence_client() -> Confluence:
    url = os.getenv("CONFLUENCE_URL", "https://confluence.sage.com")
    token = os.getenv("CONFLUENCE_TOKEN", "")
    username = os.getenv("CONFLUENCE_USERNAME", "")
    password = os.getenv("CONFLUENCE_PASSWORD", "")

    if token:
        return Confluence(url=url, token=token)
    if username and password:
        return Confluence(url=url, username=username, password=password)
    raise ValueError(
        "Set CONFLUENCE_TOKEN or CONFLUENCE_USERNAME and CONFLUENCE_PASSWORD "
        "in the environment or an ignored .env file."
    )


def normalize_storage(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def update_document(
    client: Confluence,
    path: Path,
    metadata: dict[str, Any],
    body: str,
    revision: str,
    live: bool,
    create_missing: bool,
) -> str:
    target = validate_publication(metadata, path, create_missing)
    source_url = git_source_url(revision, path)
    new_body = markdown_to_storage(metadata, body, revision, source_url)
    if target["mode"] == "create":
        if not live:
            return (
                f"DRY-RUN CREATE {metadata['id']} title={target['title']!r} "
                f"space={target['space_key']} parent={target['parent_page_id']}"
            )

        existing = client.get_page_by_title(
            space=target["space_key"], title=target["title"]
        )
        if existing:
            raise ValueError(
                f"Refusing to create {metadata['id']}: a page titled "
                f"{target['title']!r} already exists in {target['space_key']}. "
                "Record its page_id in the document instead."
            )

        created = client.create_page(
            space=target["space_key"],
            title=target["title"],
            body=new_body,
            parent_id=target["parent_page_id"],
            representation="storage",
        )
        created_id = str(created.get("id", ""))
        if not created_id:
            raise ValueError(
                f"Confluence did not return a page ID for {metadata['id']}"
            )
        return (
            f"CREATED {metadata['id']} page={created_id} "
            f"parent={target['parent_page_id']}"
        )

    page_id = target["page_id"]
    page = client.get_page_by_id(page_id, expand="version,body.storage")
    if not page:
        raise ValueError(f"Confluence page not found: {page_id}")

    actual_title = str(page["title"])
    expected_title = target["title"]
    if actual_title != expected_title:
        raise ValueError(
            f"Title mismatch for {metadata['id']}: "
            f"Confluence has {actual_title!r}, document has {expected_title!r}."
        )

    current_body = page["body"]["storage"]["value"]
    current_version = int(page["version"]["number"])
    if normalize_storage(current_body) == normalize_storage(new_body):
        return f"UNCHANGED {metadata['id']} page={page_id} v{current_version}"

    if not live:
        return (
            f"DRY-RUN {metadata['id']} page={page_id} "
            f"v{current_version} -> v{current_version + 1}"
        )

    client.update_page(
        page_id=page_id,
        title=actual_title,
        body=new_body,
        type="page",
        representation="storage",
    )
    return (
        f"UPDATED {metadata['id']} page={page_id} "
        f"v{current_version} -> v{current_version + 1}"
    )


def main() -> int:
    args = parse_args()
    if args.live and args.confirm_live != LIVE_CONFIRMATION:
        print(
            f"ERROR: --live requires --confirm-live {LIVE_CONFIRMATION}",
            file=sys.stderr,
        )
        return 2

    load_workspace_env(Path(__file__))

    documents: list[tuple[Path, dict[str, Any], str]] = []
    errors = 0
    for path in args.documents:
        try:
            metadata, body = load_document(path)
            validate_publication(metadata, path, args.create_missing)
            documents.append((path, metadata, body))
        except Exception as exc:
            print(f"ERROR {path}: {exc}", file=sys.stderr)
            errors += 1

    if errors:
        return 1

    try:
        client = confluence_client()
        revision = git_revision()
        for path, metadata, body in documents:
            print(
                update_document(
                    client,
                    path,
                    metadata,
                    body,
                    revision,
                    args.live,
                    args.create_missing,
                )
            )
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not args.live:
        print("Dry-run only. No Confluence pages were changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
