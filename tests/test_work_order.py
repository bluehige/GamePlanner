import json
from pathlib import Path
import unittest

from scripts.validate_work_order import validate_work_order


class WorkOrderValidationTests(unittest.TestCase):
    def test_example_is_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / "examples/tactical-dungeon/work-order.json").read_text(encoding="utf-8"))
        self.assertEqual([], validate_work_order(data))

    def test_scope_overlap_and_missing_fields_fail(self) -> None:
        data = {
            "work_order_id": "bad",
            "request_summary": "",
            "interpreted_goal": {},
            "source_of_truth": [],
            "in_scope": ["combat"],
            "out_of_scope": ["Combat"],
            "acceptance_criteria": [],
            "verification": [],
            "risk_tier": "high",
            "rollback": {},
        }
        errors = validate_work_order(data)
        self.assertGreaterEqual(len(errors), 8)
        self.assertTrue(any("overlap" in error for error in errors))
        self.assertTrue(any("forbidden_changes" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
