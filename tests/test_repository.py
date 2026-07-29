from pathlib import Path
import unittest

from scripts.validate_repository import EXPECTED_STAGES, validate_repository


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_contracts(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual([], validate_repository(root))
        self.assertEqual(20, len(EXPECTED_STAGES))


if __name__ == "__main__":
    unittest.main()
