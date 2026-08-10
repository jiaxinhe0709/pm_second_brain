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

HTML that must be rendered through Confluence's HTML macro must be explicitly
delimited in Markdown:

    <!-- confluence-html-macro:start -->
    <div>...</div>
    <!-- confluence-html-macro:end -->

An optional PM-friendly page layout can be requested in front matter:

    confluence:
      layout: two_left_sidebar
      toc: true

This places Confluence's native Table of Contents macro in the narrow left
column and the generated document in the wide right column.
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
HTML_MACRO_START = "<!-- confluence-html-macro:start -->"
HTML_MACRO_END = "<!-- confluence-html-macro:end -->"
HTML_MACRO_PATTERN = re.compile(
    rf"{re.escape(HTML_MACRO_START)}\s*(.*?)\s*{re.escape(HTML_MACRO_END)}",
    re.DOTALL,
)
LEFT_TOC_LAYOUT = "two_left_sidebar"
CONFLUENCE_CONFIG = ROOT_DIR / "config" / "confluence.yml"


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


def current_page_sources() -> dict[str, str]:
    if not CONFLUENCE_CONFIG.exists():
        return {}
    config = yaml.safe_load(CONFLUENCE_CONFIG.read_text(encoding="utf-8")) or {}
    if not isinstance(config, dict):
        raise ValueError(f"Invalid Confluence configuration: {CONFLUENCE_CONFIG}")
    publication = config.get("publication", {})
    if not isinstance(publication, dict):
        raise ValueError(f"Invalid publication configuration: {CONFLUENCE_CONFIG}")
    selected = publication.get("current_sources", {})
    if not isinstance(selected, dict):
        raise ValueError(
            f"publication.current_sources must be a mapping: {CONFLUENCE_CONFIG}"
        )
    return {str(page_id): str(document_id) for page_id, document_id in selected.items()}


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
        selected_source = current_page_sources().get(page_id)
        if selected_source and selected_source != str(metadata.get("id")):
            raise ValueError(
                f"Refusing to publish {metadata.get('id')} to page {page_id}: "
                f"current source is {selected_source} in config/confluence.yml"
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
    start_count = body.count(HTML_MACRO_START)
    end_count = body.count(HTML_MACRO_END)
    if start_count != end_count:
        raise ValueError(
            "Unmatched Confluence HTML macro marker: each start marker must have "
            "one end marker."
        )

    html_macros: list[tuple[str, str]] = []

    def preserve_html_macro(match: re.Match[str]) -> str:
        fragment = match.group(1).strip()
        if not fragment:
            raise ValueError("Confluence HTML macro blocks cannot be empty.")
        if "]]>" in fragment:
            raise ValueError(
                "Confluence HTML macro content cannot contain the CDATA terminator ]]>"
            )
        token = f"CONFLUENCE_HTML_MACRO_{len(html_macros)}"
        html_macros.append((token, fragment))
        return f"\n\n{token}\n\n"

    markdown_body = HTML_MACRO_PATTERN.sub(preserve_html_macro, body)
    rendered = markdown.markdown(
        markdown_body,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="xhtml",
    )
    for token, fragment in html_macros:
        macro = (
            '<ac:structured-macro ac:name="html">'
            "<ac:plain-text-body><![CDATA["
            f"{fragment}"
            "]]></ac:plain-text-body>"
            "</ac:structured-macro>"
        )
        paragraph_token = f"<p>{token}</p>"
        if paragraph_token not in rendered:
            raise ValueError(
                f"Could not restore preserved Confluence HTML macro token {token}."
            )
        rendered = rendered.replace(paragraph_token, macro, 1)
    content = banner + rendered
    confluence = metadata.get("confluence", {})
    if not isinstance(confluence, dict):
        raise ValueError("Invalid confluence metadata")

    layout = str(confluence.get("layout", "")).strip()
    toc_enabled = confluence.get("toc", False)
    if not layout:
        if toc_enabled:
            raise ValueError(
                "confluence.toc requires confluence.layout: two_left_sidebar"
            )
        return content
    if layout != LEFT_TOC_LAYOUT:
        raise ValueError(
            f"Unsupported confluence.layout {layout!r}; "
            f"supported value is {LEFT_TOC_LAYOUT!r}"
        )
    if toc_enabled is not True:
        raise ValueError(
            "confluence.layout: two_left_sidebar requires confluence.toc: true"
        )

    toc = (
        '<ac:structured-macro ac:name="toc">'
        '<ac:parameter ac:name="minLevel">2</ac:parameter>'
        '<ac:parameter ac:name="maxLevel">3</ac:parameter>'
        '<ac:parameter ac:name="style">none</ac:parameter>'
        '<ac:parameter ac:name="printable">true</ac:parameter>'
        "</ac:structured-macro>"
    )
    return (
        "<ac:layout>"
        f'<ac:layout-section ac:type="{LEFT_TOC_LAYOUT}">'
        f"<ac:layout-cell>{toc}</ac:layout-cell>"
        f"<ac:layout-cell>{content}</ac:layout-cell>"
        "</ac:layout-section>"
        "</ac:layout>"
    )


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
    page = client.get_page_by_id(page_id, expand="version,body.storage,ancestors")
    if not page:
        raise ValueError(f"Confluence page not found: {page_id}")

    actual_title = str(page["title"])
    expected_title = target["title"]
    title_changed = actual_title != expected_title

    ancestors = page.get("ancestors", [])
    actual_parent_id = str(ancestors[-1].get("id", "")) if ancestors else ""
    expected_parent_id = target["parent_page_id"]
    parent_changed = bool(expected_parent_id) and actual_parent_id != expected_parent_id

    current_body = page["body"]["storage"]["value"]
    current_version = int(page["version"]["number"])
    body_changed = normalize_storage(current_body) != normalize_storage(new_body)
    if not title_changed and not body_changed and not parent_changed:
        return f"UNCHANGED {metadata['id']} page={page_id} v{current_version}"

    rename_summary = (
        f" title={actual_title!r} -> {expected_title!r}" if title_changed else ""
    )
    parent_summary = (
        f" parent={actual_parent_id or '<root>'} -> {expected_parent_id}"
        if parent_changed
        else ""
    )
    if not live:
        return (
            f"DRY-RUN {metadata['id']} page={page_id} "
            f"v{current_version} -> v{current_version + 1}"
            f"{rename_summary}{parent_summary}"
        )

    client.update_page(
        page_id=page_id,
        title=expected_title,
        body=new_body,
        parent_id=expected_parent_id or None,
        type="page",
        representation="storage",
    )
    return (
        f"UPDATED {metadata['id']} page={page_id} "
        f"v{current_version} -> v{current_version + 1}"
        f"{rename_summary}{parent_summary}"
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
