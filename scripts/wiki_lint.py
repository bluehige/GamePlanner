#!/usr/bin/env python3
"""Lint a GamePlanner .game-wiki directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = ["SCHEMA.md", "index.md", "log.md", "current-state.md"]
REQUIRED_DIRS = [
    "raw", "project", "decisions", "incidents", "rules", "experiments",
    "playtests", "verifications", "releases", "handoffs", "_archive",
]
INCIDENT_ID = re.compile(r"^INC-\d{4}-\d{4}$")
ALLOWED_STATUSES = {
    "draft", "reproduced", "root-caused", "fixed", "verified",
    "rule-candidate", "active-rule", "closed", "superseded",
}
ALLOWED_SEVERITIES = {"minor", "major", "critical"}
REQUIRED_INCIDENT_HEADINGS = [
    "## 요청과 해석", "## 기대와 관찰", "## 재현", "## 근본 원인",
    "## 수정", "## 검증", "## 예방",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if not line.strip() or line.startswith((" ", "\t", "#")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return {}


def lint_wiki(wiki_root: Path) -> list[str]:
    wiki_root = wiki_root.resolve()
    errors: list[str] = []
    if not wiki_root.is_dir():
        return [f"wiki root does not exist: {wiki_root}"]

    for name in REQUIRED_FILES:
        path = wiki_root / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {name}")
    for name in REQUIRED_DIRS:
        if not (wiki_root / name).is_dir():
            errors.append(f"missing required directory: {name}/")

    seen_ids: dict[str, Path] = {}
    incidents_dir = wiki_root / "incidents"
    if incidents_dir.is_dir():
        for path in sorted(incidents_dir.glob("*.md")):
            if path.name.startswith("_"):
                continue
            text = path.read_text(encoding="utf-8")
            meta = parse_frontmatter(text)
            for field in ("incident_id", "title", "status", "severity", "occurred_at"):
                if not meta.get(field):
                    errors.append(f"{path.relative_to(wiki_root)}: missing frontmatter {field}")
            incident_id = meta.get("incident_id", "")
            if incident_id and not INCIDENT_ID.match(incident_id):
                errors.append(f"{path.relative_to(wiki_root)}: invalid incident_id {incident_id}")
            if incident_id in seen_ids:
                errors.append(
                    f"duplicate incident_id {incident_id}: "
                    f"{seen_ids[incident_id].relative_to(wiki_root)}, {path.relative_to(wiki_root)}"
                )
            elif incident_id:
                seen_ids[incident_id] = path
            if incident_id and not path.stem.startswith(incident_id):
                errors.append(f"{path.relative_to(wiki_root)}: filename must start with {incident_id}")
            status = meta.get("status")
            if status and status not in ALLOWED_STATUSES:
                errors.append(f"{path.relative_to(wiki_root)}: invalid status {status}")
            severity = meta.get("severity")
            if severity and severity not in ALLOWED_SEVERITIES:
                errors.append(f"{path.relative_to(wiki_root)}: invalid severity {severity}")
            if meta.get("occurred_at") and not re.match(r"^\d{4}-\d{2}-\d{2}$", meta["occurred_at"]):
                errors.append(f"{path.relative_to(wiki_root)}: occurred_at must be YYYY-MM-DD")
            for heading in REQUIRED_INCIDENT_HEADINGS:
                if heading not in text:
                    errors.append(f"{path.relative_to(wiki_root)}: missing heading '{heading}'")
            if status in {"active-rule", "closed"} and "- 결과:" not in text:
                errors.append(f"{path.relative_to(wiki_root)}: terminal incident requires verification result")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wiki_root", type=Path)
    args = parser.parse_args(argv)
    errors = lint_wiki(args.wiki_root)
    if errors:
        print(f"Wiki lint FAILED with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Wiki lint PASS: {args.wiki_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
