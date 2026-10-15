from pathlib import Path
import sys
import unittest
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import update_confluence_pages as publisher


class ConfluenceChangeHistoryTests(unittest.TestCase):
    def metadata(self) -> dict:
        return {
            "id": "TEST-CONFLUENCE-CHANGE-HISTORY",
            "title": "Change History Test",
            "type": "publication-test",
            "status": "draft",
            "owner": "Test",
            "updated": "2026-08-26",
            "confluence": {
                "publish": True,
                "space_key": "DNBU",
                "parent_page_id": "",
                "page_id": "999999999",
                "title": "Change History Test",
                "layout": "two_left_sidebar",
                "toc": True,
            },
        }

    def test_config_enables_ten_change_history_versions(self) -> None:
        self.assertEqual(publisher.configured_change_history_limit(), 10)

    def test_publication_rejects_manual_history_headings(self) -> None:
        path = ROOT / "prds" / "example.md"
        for heading in ("## Change log", "## Revision history", "## Decisions and change log"):
            with self.subTest(heading=heading):
                with self.assertRaisesRegex(ValueError, "native Change History"):
                    publisher.validate_no_manual_history(f"# Test\n\n{heading}\n", path)

        publisher.validate_no_manual_history(
            "# Test\n\n## Revision overview\n\nProduct changes.\n", path
        )

    @patch.object(publisher, "configured_change_history_limit", return_value=None)
    def test_publication_requires_native_history(self, _history_limit: MagicMock) -> None:
        with self.assertRaisesRegex(ValueError, "Publication requires Confluence Change History"):
            publisher.required_change_history_limit()

    def test_storage_appends_native_change_history_macro(self) -> None:
        storage = publisher.markdown_to_storage(
            self.metadata(),
            "# Test\n\n## Outcome\n\nContent.",
            "abcdef1234567890",
            "https://github.example/source",
            change_history_limit=10,
        )

        self.assertEqual(storage.count('ac:name="change-history"'), 1)
        self.assertIn(
            '<ac:parameter ac:name="limit">10</ac:parameter>', storage
        )
        self.assertGreater(
            storage.index("Confluence page history"), storage.index("<h1>Test</h1>")
        )
        self.assertEqual(storage.count('ac:name="toc"'), 1)

    def test_storage_can_disable_change_history(self) -> None:
        storage = publisher.markdown_to_storage(
            self.metadata(),
            "# Test",
            "abcdef1234567890",
            None,
            change_history_limit=None,
        )

        self.assertNotIn('ac:name="change-history"', storage)

    def test_source_links_resolve_angle_brackets_spaces_and_unicode(self) -> None:
        storage = publisher.storage_with_drawio(
            self.metadata(),
            "[Source](<../context/source file.pdf>)\n\n"
            "[Unicode](<../context/café.pdf>)\n\n"
            "[Plain](../specs/plain.md)\n\n"
            "[Anchor](<#section>)\n\n"
            "[External](<https://example.com/source>)",
            "abcdef",
            "https://github.example/repo/blob/abcdef/specs/spec.md",
            [],
            {},
        )

        for target in (
            "https://github.example/repo/blob/abcdef/context/source%20file.pdf",
            "https://github.example/repo/blob/abcdef/context/caf%C3%A9.pdf",
            "https://github.example/repo/blob/abcdef/specs/plain.md",
            "#section",
            "https://example.com/source",
        ):
            with self.subTest(target=target):
                self.assertIn(f'href="{target}"', storage)
        self.assertNotIn("&lt;../context/", storage)

    def test_storage_rejects_invalid_change_history_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive integer"):
            publisher.markdown_to_storage(
                self.metadata(),
                "# Test",
                "abcdef1234567890",
                None,
                change_history_limit=0,
            )

    def test_storage_comparison_ignores_confluence_generated_macro_ids(self) -> None:
        generated = '<ac:structured-macro ac:name="toc"></ac:structured-macro>'
        saved = (
            '<ac:structured-macro ac:name="toc" ac:schema-version="1" '
            'ac:macro-id="cf0bfca7-3416-4602-a41f-1b9b7f8d6788"></ac:structured-macro>'
        )
        self.assertEqual(
            publisher.normalize_storage(generated),
            publisher.normalize_storage(saved),
        )

    @patch.object(publisher, "configured_change_history_limit", return_value=10)
    @patch.object(
        publisher,
        "git_source_url",
        return_value="https://github.example/source",
    )
    def test_live_update_sets_git_version_comment(
        self, _source_url: MagicMock, _history_limit: MagicMock
    ) -> None:
        client = MagicMock()
        client.get_page_by_id.return_value = {
            "title": "Change History Test",
            "version": {"number": 3},
            "body": {"storage": {"value": "<p>old</p>"}},
            "ancestors": [],
        }
        revision = "abcdef1234567890"

        result = publisher.update_document(
            client=client,
            path=ROOT / "tests" / "fixtures" / "confluence-left-sidebar-layout-test.md",
            metadata=self.metadata(),
            body="# Test\n\nChanged.",
            revision=revision,
            live=True,
            create_missing=False,
        )

        self.assertIn("v3 -> v4", result)
        call = client.update_page.call_args.kwargs
        self.assertEqual(
            call["version_comment"],
            "TEST-CONFLUENCE-CHANGE-HISTORY published from Git abcdef123456 "
            "(document updated 2026-08-26)",
        )
        self.assertIn('ac:name="change-history"', call["body"])


class DrawioPublicationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.path = ROOT / "prds" / "PRD-SEI-244-e-invoicing-process-flow-specification.md"
        self.metadata, self.body = publisher.load_document(self.path)
        self.assets = publisher.drawio_assets(self.path, self.body)

    def test_eight_diagrams_render_as_native_macros(self) -> None:
        self.assertEqual(len(self.assets), 8)
        storage = publisher.storage_with_drawio(
            self.metadata,
            self.body,
            "abcdef1234567890",
            "https://github.com/example/repo/blob/abcdef1234567890/prds/PRD-SEI-244-e-invoicing-process-flow-specification.md",
            self.assets,
            {},
        )
        self.assertEqual(storage.count('ac:name="drawio"'), 8)
        self.assertNotIn("../assets/diagrams/", storage)
        self.assertIn('ac:name="change-history"', storage)

    def test_uploads_both_editable_source_and_preview(self) -> None:
        client = MagicMock()
        client.get_attachments_from_content.return_value = {
            "results": [
                {"title": asset.name, "version": {"number": 1}}
                for asset in self.assets
            ]
        }
        revisions = publisher.upload_drawio_assets(client, "12345", self.assets)
        self.assertEqual(client.attach_file.call_count, 16)
        self.assertEqual(revisions, {asset.name: 1 for asset in self.assets})
        self.assertEqual(
            client.get_attachments_from_content.call_args.kwargs["expand"], "version"
        )

    @patch.object(publisher, "git_source_url", return_value=None)
    def test_create_places_macros_under_configured_parent(self, _source_url: MagicMock) -> None:
        client = MagicMock()
        client.get_page_by_title.return_value = None
        client.create_page.return_value = {"id": "12345"}
        metadata = dict(self.metadata)
        metadata["confluence"] = dict(self.metadata["confluence"], page_id="")
        with patch.object(
            publisher,
            "upload_drawio_assets",
            return_value={asset.name: 1 for asset in self.assets},
        ):
            result = publisher.update_document(
                client,
                self.path,
                metadata,
                self.body,
                "abcdef1234567890",
                live=True,
                create_missing=True,
            )
        self.assertIn("parent=866150169", result)
        self.assertEqual(client.create_page.call_args.kwargs["parent_id"], "866150169")
        self.assertEqual(client.update_page.call_args.kwargs["body"].count('ac:name="drawio"'), 8)
        self.assertIn("PRD-SEI-244 published from Git abcdef123456", client.update_page.call_args.kwargs["version_comment"])


if __name__ == "__main__":
    unittest.main()
