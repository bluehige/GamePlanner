from pathlib import Path
import tempfile
import unittest

from scripts.wiki_lint import lint_wiki


class WikiLintTests(unittest.TestCase):
    def test_example_wiki_is_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        wiki = root / "examples/tactical-dungeon/.game-wiki"
        self.assertEqual([], lint_wiki(wiki))

    def test_missing_structure_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            errors = lint_wiki(Path(temp))
            self.assertTrue(any("SCHEMA.md" in error for error in errors))
            self.assertTrue(any("incidents/" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
