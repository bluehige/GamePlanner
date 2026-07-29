#!/usr/bin/env python3
"""Validate a GamePlanner Work Order JSON file without jsonschema."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

WORK_ORDER_ID = re.compile(r"^WO-\d{4}-\d{4}$")
RISK_TIERS = {"low", "medium", "high", "prototype"}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(nonempty_string(item) for item in value)


def validate_work_order(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root must be a JSON object"]

    work_order_id = data.get("work_order_id")
    if not nonempty_string(work_order_id) or not WORK_ORDER_ID.match(work_order_id):
        errors.append("work_order_id must match WO-YYYY-NNNN")
    if not nonempty_string(data.get("request_summary")):
        errors.append("request_summary must be a non-empty string")

    goal = data.get("interpreted_goal")
    if not isinstance(goal, dict):
        errors.append("interpreted_goal must be an object")
    else:
        for field in ("player_outcome", "system_outcome"):
            if not nonempty_string(goal.get(field)):
                errors.append(f"interpreted_goal.{field} must be a non-empty string")

    for field in ("source_of_truth", "in_scope", "out_of_scope", "acceptance_criteria", "verification"):
        if not nonempty_string_list(data.get(field)):
            errors.append(f"{field} must be a non-empty array of non-empty strings")

    for field in ("affected_systems", "forbidden_changes", "assumptions"):
        value = data.get(field, [])
        if not isinstance(value, list) or not all(nonempty_string(item) for item in value):
            errors.append(f"{field} must be an array of non-empty strings when present")

    risk = data.get("risk_tier")
    if risk not in RISK_TIERS:
        errors.append(f"risk_tier must be one of {', '.join(sorted(RISK_TIERS))}")

    rollback = data.get("rollback")
    if not isinstance(rollback, dict):
        errors.append("rollback must be an object")
    else:
        for field in ("baseline_sha", "strategy"):
            if not nonempty_string(rollback.get(field)):
                errors.append(f"rollback.{field} must be a non-empty string")

    in_scope = {item.strip().casefold() for item in data.get("in_scope", []) if isinstance(item, str)}
    out_scope = {item.strip().casefold() for item in data.get("out_of_scope", []) if isinstance(item, str)}
    overlap = sorted(in_scope & out_scope)
    if overlap:
        errors.append(f"in_scope and out_of_scope overlap: {', '.join(overlap)}")

    if risk in {"medium", "high"} and not data.get("affected_systems"):
        errors.append("medium/high risk work orders require affected_systems")
    if risk == "high" and not data.get("forbidden_changes"):
        errors.append("high risk work orders require forbidden_changes")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Work Order validation FAILED: {exc}")
        return 1
    errors = validate_work_order(data)
    if errors:
        print(f"Work Order validation FAILED with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Work Order validation PASS: {data['work_order_id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
