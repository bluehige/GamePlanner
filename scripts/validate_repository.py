#!/usr/bin/env python3
"""Validate GamePlanner repository structure without third-party packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

EXPECTED_STAGES = [f"{i:02d}" for i in range(19)] + ["90"]
REQUIRED_SKILL_HEADINGS = [
    "## 사용 시점",
    "## 입력",
    "## 절차",
    "## 산출물",
    "## 완료 게이트",
]
REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "AGENTS.md",
    "CATALOG.md",
    "THIRD_PARTY_NOTICES.md",
    ".codex-plugin/plugin.json",
    "external/UPSTREAMS.lock.json",
    "schemas/work-order.schema.json",
    "schemas/incident.schema.json",
    "schemas/upstreams.schema.json",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return {}


def markdown_links(text: str) -> Iterable[str]:
    pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for match in pattern.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        yield target


def validate_local_links(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for md_path in sorted(repo_root.rglob("*.md")):
        if any(part.startswith(".") and part not in {".github", ".game-wiki"} for part in md_path.parts):
            continue
        text = md_path.read_text(encoding="utf-8")
        for target in markdown_links(text):
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part or "{{" in path_part:
                continue
            resolved = (md_path.parent / path_part).resolve()
            try:
                resolved.relative_to(repo_root.resolve())
            except ValueError:
                errors.append(f"{md_path.relative_to(repo_root)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{md_path.relative_to(repo_root)}: broken local link: {target}")
    return errors


def load_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None


def validate_repository(repo_root: Path) -> list[str]:
    repo_root = repo_root.resolve()
    errors: list[str] = []

    for rel in REQUIRED_ROOT_FILES:
        if not (repo_root / rel).exists():
            errors.append(f"missing required file: {rel}")

    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        errors.append("missing skills directory")
        return errors

    stage_to_dir: dict[str, Path] = {}
    skill_names: set[str] = set()
    pattern = re.compile(r"^(\d{2})-(.+)$")

    for directory in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        match = pattern.match(directory.name)
        if not match:
            errors.append(f"invalid skill directory name: {directory.name}")
            continue
        stage, slug = match.groups()
        if stage in stage_to_dir:
            errors.append(f"duplicate stage {stage}: {stage_to_dir[stage].name}, {directory.name}")
        stage_to_dir[stage] = directory

        skill_path = directory / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"{directory.name}: missing SKILL.md")
            continue
        text = skill_path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        for field in ("name", "description"):
            if not meta.get(field):
                errors.append(f"{skill_path.relative_to(repo_root)}: missing frontmatter {field}")
        name = meta.get("name", "")
        if name and name != slug:
            errors.append(f"{skill_path.relative_to(repo_root)}: name '{name}' must match directory slug '{slug}'")
        if name in skill_names:
            errors.append(f"duplicate skill name: {name}")
        if name:
            skill_names.add(name)
        for heading in REQUIRED_SKILL_HEADINGS:
            if heading not in text:
                errors.append(f"{skill_path.relative_to(repo_root)}: missing heading '{heading}'")

    actual_stages = sorted(stage_to_dir)
    missing = [stage for stage in EXPECTED_STAGES if stage not in stage_to_dir]
    extra = [stage for stage in actual_stages if stage not in EXPECTED_STAGES]
    if missing:
        errors.append(f"missing numbered stages: {', '.join(missing)}")
    if extra:
        errors.append(f"unexpected numbered stages: {', '.join(extra)}")

    plugin_path = repo_root / ".codex-plugin/plugin.json"
    if plugin_path.exists():
        plugin = load_json(plugin_path, errors)
        if isinstance(plugin, dict):
            if plugin.get("name") != "game-planner":
                errors.append(".codex-plugin/plugin.json: name must be game-planner")
            if plugin.get("skills") != "./skills/":
                errors.append(".codex-plugin/plugin.json: skills must be ./skills/")
            if plugin.get("repository") != "https://github.com/bluehige/GamePlanner":
                errors.append(".codex-plugin/plugin.json: repository URL mismatch")

    upstream_path = repo_root / "external/UPSTREAMS.lock.json"
    if upstream_path.exists():
        upstream_lock = load_json(upstream_path, errors)
        if isinstance(upstream_lock, dict):
            upstreams = upstream_lock.get("upstreams")
            if not isinstance(upstreams, list) or not upstreams:
                errors.append("external/UPSTREAMS.lock.json: upstreams must be a non-empty array")
            else:
                ids: set[str] = set()
                for index, item in enumerate(upstreams):
                    where = f"external/UPSTREAMS.lock.json upstream[{index}]"
                    if not isinstance(item, dict):
                        errors.append(f"{where}: must be an object")
                        continue
                    for field in ("id", "stage", "url", "ref", "license", "integration", "role"):
                        if not isinstance(item.get(field), str) or not item[field].strip():
                            errors.append(f"{where}: missing non-empty {field}")
                    upstream_id = item.get("id")
                    if isinstance(upstream_id, str):
                        if upstream_id in ids:
                            errors.append(f"{where}: duplicate id {upstream_id}")
                        ids.add(upstream_id)
                    stage = item.get("stage")
                    if isinstance(stage, str) and stage not in EXPECTED_STAGES:
                        errors.append(f"{where}: unknown stage {stage}")
                    url = item.get("url")
                    if isinstance(url, str) and not url.startswith("https://"):
                        errors.append(f"{where}: URL must use https")

    for schema_path in sorted((repo_root / "schemas").glob("*.json")):
        load_json(schema_path, errors)

    errors.extend(validate_local_links(repo_root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = validate_repository(args.root)
    if errors:
        print(f"GamePlanner validation FAILED with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"GamePlanner validation PASS: {len(EXPECTED_STAGES)} numbered skills and repository contracts are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
