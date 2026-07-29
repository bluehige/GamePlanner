from pathlib import Path
import unittest

from scripts.install_upstreams import installable, load_upstreams, select_upstreams


class InstallUpstreamsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = Path(__file__).resolve().parents[1]
        cls.upstreams = load_upstreams(root / "external/UPSTREAMS.lock.json")

    def test_catalog_contains_installable_and_reference_only_entries(self) -> None:
        self.assertTrue(any(installable(item) for item in self.upstreams))
        self.assertTrue(any(not installable(item) for item in self.upstreams))

    def test_select_by_stage(self) -> None:
        selected = select_upstreams(self.upstreams, stages=["08"])
        self.assertEqual(["game-ui-ux-rules"], [item["id"] for item in selected])

    def test_concept_only_gist_is_never_installable(self) -> None:
        selected = select_upstreams(self.upstreams, ids=["karpathy-llm-wiki"])
        self.assertEqual([], selected)


if __name__ == "__main__":
    unittest.main()
