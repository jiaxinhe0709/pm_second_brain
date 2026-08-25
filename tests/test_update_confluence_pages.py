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
            "updated": "2026-08-25",
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

    def test_storage_includes_native_change_history_macro(self) -> None:
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
        self.assertLess(
            storage.index("Publication history"), storage.index("<h1>Test</h1>")
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

    def test_storage_rejects_invalid_change_history_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive integer"):
            publisher.markdown_to_storage(
                self.metadata(),
                "# Test",
                "abcdef1234567890",
                None,
                change_history_limit=0,
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
            "(document updated 2026-08-25)",
        )
        self.assertIn('ac:name="change-history"', call["body"])


if __name__ == "__main__":
    unittest.main()
