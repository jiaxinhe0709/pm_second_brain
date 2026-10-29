"""Exercise source drift and historical/current-reference boundaries."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from validate_spfe_sources import MANIFEST, validate


class SourceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.current = Path("context/WSDL servicios web - PRE_current")
        self.old = Path("context/WSDL servicios web - PRE_old")
        wsdl = b'''<definitions xmlns="http://schemas.xmlsoap.org/wsdl/"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema"><types><xsd:schema>
            <xsd:import schemaLocation="missing.xsd"/>
            </xsd:schema></types></definitions>'''
        new_entry = self.write_source(self.current / "Example.wsdl", wsdl)
        old_entry = self.write_source(self.old / "Example.wsdl", wsdl)
        self.manifest = {
            "sources": [new_entry],
            "current_wsdl_baseline": {
                "root": str(self.current), "release_date": "2026-10-29",
                "reviewed_on": "2026-10-29",
                "missing_schema_gates": {str(self.current / "missing.xsd"): "SPFE-Q04"},
            },
            "historical_wsdl_releases": [{
                "root": str(self.old), "release_date": "2026-10-16",
                "sources": [old_entry],
            }],
        }
        self.save_manifest()
        self.document = self.root / "specs/current.md"
        self.document.parent.mkdir()
        self.document.write_text(f"[Contract](<../{self.current}/Example.wsdl>)\n")

    def write_source(self, relative, data, kind="wsdl", source_id="SPFE-S16"):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return {"path": str(relative), "bytes": len(data), "kind": kind,
                "source_id": source_id, "sha256": hashlib.sha256(data).hexdigest()}

    def save_manifest(self):
        path = self.root / MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.manifest))

    def assert_error(self, expected):
        errors = validate(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_baseline_with_explicit_missing_schema_gate(self):
        self.assertEqual(validate(self.root), [])

    def test_changed_source_is_rejected(self):
        path = self.root / self.current / "Example.wsdl"
        path.write_bytes(path.read_bytes() + b"\n")
        self.assert_error("Source bytes changed")

    def test_new_release_is_detected_before_any_spec_references_it(self):
        path = self.root / "context/WSDL servicios web - PRE_next/New.wsdl"
        path.parent.mkdir()
        path.write_text("<definitions/>")
        self.assert_error("Unregistered contract evidence")

    def test_active_reference_to_historical_contract_is_rejected(self):
        self.document.write_text(f"[Old](<../{self.old}/Example.wsdl>)")
        self.assert_error("Stale contract reference")

    def test_archived_reference_remains_historical(self):
        archive = self.root / "specs/archive/history.md"
        archive.parent.mkdir()
        archive.write_text(f"[Old](<../../{self.old}/Example.wsdl>)")
        self.assertEqual(validate(self.root), [])

    def test_broken_current_reference_is_rejected(self):
        self.document.write_text(f"[Absent](<../{self.current}/Absent.wsdl>)")
        self.assert_error("Broken/unregistered contract reference")

    def test_current_cannot_be_older_than_a_registered_release(self):
        self.manifest["historical_wsdl_releases"][0]["release_date"] = "2026-10-30"
        self.save_manifest()
        self.assert_error("older than a registered release")

    def test_unreviewed_baseline_is_rejected(self):
        self.manifest["current_wsdl_baseline"]["reviewed_on"] = "2026-10-28"
        self.save_manifest()
        self.assert_error("has not been reviewed")

    def test_missing_import_needs_an_explicit_gate(self):
        self.manifest["current_wsdl_baseline"]["missing_schema_gates"] = {}
        self.save_manifest()
        self.assert_error("Missing schema without an evidence gate")

    def test_added_schema_requires_reindex_and_gate_review(self):
        entry = self.write_source(self.current / "missing.xsd", b'<schema/>', "xsd", "SPFE-S19")
        self.manifest["sources"].append(entry)
        self.save_manifest()
        self.assert_error("Obsolete missing-schema gate")
        self.manifest["current_wsdl_baseline"]["missing_schema_gates"] = {}
        self.save_manifest()
        self.assertEqual(validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
