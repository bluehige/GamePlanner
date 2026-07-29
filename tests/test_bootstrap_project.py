from pathlib import Path
import json
import tempfile
import unittest

from scripts.bootstrap_project import bootstrap
from scripts.wiki_lint import lint_wiki


class BootstrapProjectTests(unittest.TestCase):
    def test_bootstrap_creates_contracts_skill_and_wiki(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "my-game"
            created, skipped = bootstrap(
                target=target,
                slug="my-game",
                game_title="My Game",
                engine="Godot 4.5",
                platforms=["Windows", "Linux"],
                genre="Strategy",
            )
            self.assertGreater(len(created), 20)
            self.assertEqual([], skipped)
            self.assertTrue((target / "docs/foundation/GAME_CONTRACT.md").exists())
            self.assertTrue((target / ".agents/skills/my-game-foundation/SKILL.md").exists())
            config = json.loads((target / ".game-planner/config.json").read_text(encoding="utf-8"))
            self.assertEqual("Godot 4.5", config["engine"])
            self.assertEqual([], lint_wiki(target / ".game-wiki"))

    def test_bootstrap_does_not_overwrite_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "my-game"
            bootstrap(target, "my-game", "My Game", "Godot", ["Windows"], "RPG")
            contract = target / "docs/foundation/GAME_CONTRACT.md"
            contract.write_text("custom\n", encoding="utf-8")
            _, skipped = bootstrap(target, "my-game", "My Game", "Godot", ["Windows"], "RPG")
            self.assertIn(contract, skipped)
            self.assertEqual("custom\n", contract.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
