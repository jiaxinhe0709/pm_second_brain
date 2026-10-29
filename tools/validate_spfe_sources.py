#!/usr/bin/env python3
"""Check the reviewed local SPFE baseline. Does not poll AEAT or prove readiness."""

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


MANIFEST = Path("assets/regulatory/spain/spfe/source-manifest.json")
XSD = "{http://www.w3.org/2001/XMLSchema}"
LINK = re.compile(r"\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)")


def validate(root):
    root = Path(root).resolve()
    errors = []
    try:
        manifest = json.loads((root / MANIFEST).read_text())
        current = manifest["current_wsdl_baseline"]
        history = manifest["historical_wsdl_releases"]
        sources = manifest["sources"]
        current_dir = (root / current["root"]).resolve()
        releases = [current, *history]
        dates = [date.fromisoformat(item["release_date"]) for item in releases]
        if dates[0] != max(dates):
            errors.append("Current WSDL baseline is older than a registered release.")
        reviewed = date.fromisoformat(current["reviewed_on"])
        if reviewed < dates[0]:
            errors.append("Current WSDL baseline has not been reviewed since its release.")
        if not current_dir.is_dir():
            errors.append(f"Missing current release folder: {current['root']}")
        if len({item["root"] for item in releases}) != len(releases):
            errors.append("Release roots must be distinct.")
        source_ids = [item["source_id"] for item in sources]
        if len(set(source_ids)) != len(source_ids):
            errors.append("Duplicate source ID in current source inventory.")
        entries = sources + [item for release in history for item in release["sources"]]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"Invalid SPFE manifest: {exc}"]

    registered = set()
    for entry in entries:
        try:
            path = (root / entry["path"]).resolve()
            if not path.is_relative_to(root):
                errors.append(f"Source path escapes repository: {entry['path']}")
                continue
            if path in registered:
                errors.append(f"Duplicate source path: {entry['path']}")
            registered.add(path)
            data = path.read_bytes()
            if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                errors.append(f"Source bytes changed; review and reindex: {entry['path']}")
            if entry.get("text_extract"):
                extract = (root / entry["text_extract"]).read_bytes()
                if hashlib.sha256(extract).hexdigest() != entry["extract_sha256"]:
                    errors.append(f"Text extract changed: {entry['text_extract']}")
        except (OSError, KeyError) as exc:
            errors.append(f"Missing/invalid source entry {entry.get('source_id')}: {exc}")

    # New files require review even if nobody has linked them from a spec yet.
    for path in (root / "context").rglob("*"):
        if not any(part.startswith("WSDL servicios web - PRE") for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in {".wsdl", ".xsd", ".xml", ".txt"}:
            if path.resolve() not in registered:
                errors.append(f"Unregistered contract evidence; review release: {path.relative_to(root)}")

    # Parse imports rather than trusting the inventory's local_exists flag.
    missing = set()
    current_sources = [item for item in sources if (root / item["path"]).resolve().is_relative_to(current_dir)]
    if not any(item.get("kind") == "wsdl" for item in current_sources):
        errors.append("Current release has no registered WSDL sources.")
    for entry in current_sources:
        path = root / entry["path"]
        if path.suffix.lower() not in {".wsdl", ".xsd"} or not path.is_file():
            continue
        try:
            document = ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"Invalid XML in {entry['path']}: {exc}")
            continue
        for element in document.iter():
            location = element.get("schemaLocation")
            if element.tag not in {XSD + "import", XSD + "include", XSD + "redefine"} or not location:
                continue
            if urlsplit(location).scheme:
                errors.append(f"Unqualified remote schema dependency in {entry['path']}: {location}")
                continue
            target = (path.parent / unquote(location)).resolve()
            if not target.is_relative_to(current_dir):
                errors.append(f"Schema dependency outside current release in {entry['path']}: {location}")
            elif not target.is_file():
                missing.add(target.relative_to(root).as_posix())
            elif target not in registered:
                errors.append(f"Unregistered schema dependency: {target.relative_to(root)}")
    allowed = current.get("missing_schema_gates", {})
    for path in sorted(missing - allowed.keys()):
        errors.append(f"Missing schema without an evidence gate: {path}")
    for path in sorted(allowed.keys() - missing):
        errors.append(f"Obsolete missing-schema gate; review and reindex: {path}")
    for path, gate in allowed.items():
        if not gate:
            errors.append(f"Missing schema needs a named evidence gate: {path}")

    # Current specs must cite current contracts. Archives may cite historical ones.
    for document in (root / "specs").rglob("*.md"):
        archived = "archive" in document.relative_to(root / "specs").parts
        for match in LINK.finditer(document.read_text()):
            href = match.group(1) or match.group(2)
            if urlsplit(href).scheme or href.startswith("#"):
                continue
            target = (document.parent / unquote(href.split("#", 1)[0])).resolve()
            is_contract = "WSDL servicios web - PRE" in str(target) or target in registered and target.suffix == ".wsdl"
            if not is_contract:
                continue
            label = f"{document.relative_to(root)}: {href}"
            if not target.is_file() or target not in registered:
                errors.append(f"Broken/unregistered contract reference: {label}")
            elif not archived and not target.is_relative_to(current_dir):
                errors.append(f"Stale contract reference in current spec: {label}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("SPFE source validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    manifest = json.loads((args.root / MANIFEST).read_text())
    current = manifest["current_wsdl_baseline"]
    print(f"SPFE sources OK: reviewed local PRE baseline {current['release_date']}.")
    for path, gate in current.get("missing_schema_gates", {}).items():
        print(f"OPEN {gate}: {path}")
    print("Checks identify source currency and integrity; runtime qualification remains separate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
