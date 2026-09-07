"""Metadata and safe-path tests, not tests of the findings' scientific truth."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_finding_register as register


class FindingRegisterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "evidence").mkdir()
        (self.root / "evidence/example.md").write_text("Fixture, no truth claim.\n", encoding="utf-8")
        source_path = self.root / register.SOURCE_REGISTER_PATH
        source_path.parent.mkdir(parents=True)
        source_path.write_text(
            "# Register\nH999 appears in prose, not a source row.\n"
            "| ID | Title |\n|---|---|\n| H003 | Book |\n| M005 | Reference |\n",
            encoding="utf-8")
        self.document = {
            "schema_version": 1,
            "updated": "2026-09-06",
            "scope": "Metadata fixture only.",
            "findings": [{
                "finding_id": "FIND-001", "kind": "own_diagnostic",
                "claim": "Fixture claim.", "source_ids": ["H003"],
                "source_locator": "Fixture page.", "assumptions": "Fixture assumptions.",
                "scope": "Fixture scope.", "not_established": "Scientific truth.",
                "evidence_paths": ["evidence/example.md"],
                "reproduction": "Do not execute this string.", "next_check": "Manual review.",
            }],
        }

    def errors(self, document):
        return register.validate_register(document, root=self.root, source_ids={"H003", "M005"})

    def write_register(self, content):
        path = self.root / register.REGISTER_PATH
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_valid_fixture_source_parser_and_cli_scope(self):
        self.assertEqual(register.read_source_ids(self.root / register.SOURCE_REGISTER_PATH), {"H003", "M005"})
        for kind in register.KINDS:
            self.document["findings"][0]["kind"] = kind
            self.assertEqual(self.errors(self.document), [])
        self.write_register(json.dumps(self.document))
        self.assertEqual(register.validate_file(self.root), [])
        with patch.object(register, "validate_file", return_value=[]), patch("builtins.print") as printed:
            self.assertEqual(register.main([]), 0)
            self.assertIn("keine Wahrheitspruefung", printed.call_args.args[0])
        with patch.object(register, "validate_file", return_value=["fixture error"]), patch("builtins.print"):
            self.assertEqual(register.main([]), 1)

    def test_actual_repository_register(self):
        self.assertEqual(register.validate_file(), [])

    def test_top_schema_types_and_iso_date(self):
        for field, value in (("schema_version", True), ("schema_version", 1.0),
                             ("schema_version", 2), ("updated", "2026-02-30"),
                             ("updated", "20260906"), ("updated", "2026-9-06"),
                             ("updated", None), ("scope", "  "),
                             ("findings", []), ("findings", {})):
            with self.subTest(field=field, value=value):
                doc = deepcopy(self.document)
                doc[field] = value
                self.assertTrue(self.errors(doc))
        for doc in ([], None, {}, {**self.document, "extra": 1}):
            self.assertTrue(self.errors(doc))

    def test_finding_exact_fields_nonempty_strings_and_kind(self):
        for field in register.FINDING_FIELDS - register.LIST_FIELDS:
            for value in (None, " ", 7, []):
                with self.subTest(field=field, value=value):
                    doc = deepcopy(self.document)
                    doc["findings"][0][field] = value
                    self.assertTrue(self.errors(doc))
        for replacement in (None, {}, {**self.document["findings"][0], "extra": "x"},
                            {**self.document["findings"][0], "kind": "truth_verified"}):
            doc = deepcopy(self.document)
            doc["findings"] = [replacement]
            self.assertTrue(self.errors(doc))
        for field in register.FINDING_FIELDS:
            doc = deepcopy(self.document)
            del doc["findings"][0][field]
            self.assertTrue(self.errors(doc))

    def test_finding_ids_are_formatted_and_unique(self):
        for finding_id in ("FIND-000", "FIND-1", "FIND-1000", "find-001", " FIND-001"):
            doc = deepcopy(self.document)
            doc["findings"][0]["finding_id"] = finding_id
            self.assertTrue(self.errors(doc))
        doc = deepcopy(self.document)
        doc["findings"].append(deepcopy(doc["findings"][0]))
        self.assertTrue(any("duplicate" in error for error in self.errors(doc)))
        doc["findings"][1]["finding_id"] = "FIND-002"
        self.assertEqual(self.errors(doc), [])

    def test_lists_and_known_source_ids(self):
        for field in register.LIST_FIELDS:
            for value in ([], "H003", [None], [" "], [17]):
                with self.subTest(field=field, value=value):
                    doc = deepcopy(self.document)
                    doc["findings"][0][field] = value
                    self.assertTrue(self.errors(doc))
        doc = deepcopy(self.document)
        doc["findings"][0]["source_ids"] = ["H999"]
        self.assertTrue(any("unknown source ID" in error for error in self.errors(doc)))

    def test_unsafe_missing_directory_and_resolved_escape_paths(self):
        for path in ("/evidence/example.md", "../example.md", "evidence/../evidence/example.md",
                     "evidence\\example.md", "C:/example.md", "evidence/example.md:stream",
                     "//host/share/file", "bad\x00name", "missing.md", "evidence"):
            with self.subTest(path=path):
                doc = deepcopy(self.document)
                doc["findings"][0]["evidence_paths"] = [path]
                self.assertTrue(self.errors(doc))
        # No symlink privileges required: simulate its resolved external target.
        with patch.object(Path, "resolve", return_value=self.root.parent / "outside.md"):
            error = register._evidence_error("evidence/link.md", self.root)
        self.assertIn("leaves the repository root", error)

    def test_read_failures_and_duplicate_json_keys(self):
        self.assertTrue(register.validate_file(self.root))
        for content in ("{", '{"schema_version":1,"schema_version":1}',
                        json.dumps(self.document).replace('"kind": "own_diagnostic"',
                                                        '"kind": "own_diagnostic", "kind": "own_diagnostic"')):
            with self.subTest(content=content):
                self.write_register(content)
                self.assertTrue(register.validate_file(self.root))
        self.write_register(json.dumps(self.document))
        (self.root / register.SOURCE_REGISTER_PATH).write_text("No table IDs here.", encoding="utf-8")
        self.assertTrue(register.validate_file(self.root))


if __name__ == "__main__":
    unittest.main()
