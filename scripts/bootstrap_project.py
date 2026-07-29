#!/usr/bin/env python3
"""Bootstrap GamePlanner contracts, project skill, and LLM Wiki in a game repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = REPO_ROOT / "templates"


def render_template(name: str, replacements: dict[str, str]) -> str:
    text = (TEMPLATES / name).read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def write_file(path: Path, content: str, force: bool, created: list[Path], skipped: list[Path]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        skipped.append(path)
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    created.append(path)


def valid_slug(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value))


def bootstrap(
    target: Path,
    slug: str,
    game_title: str,
    engine: str,
    platforms: list[str],
    genre: str,
    force: bool = False,
) -> tuple[list[Path], list[Path]]:
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    skipped: list[Path] = []
    platform_text = ", ".join(platforms) if platforms else "UNSET"
    replacements = {
        "project_slug": slug,
        "game_title": game_title,
        "engine": engine,
        "platforms": platform_text,
        "genre": genre,
    }

    mapping = {
        "docs/foundation/GAME_CONTRACT.md": "GAME_CONTRACT.template.md",
        "docs/foundation/CONTEXT.md": "CONTEXT.template.md",
        "docs/foundation/DECISION_LOG.md": "DECISION_LOG.template.md",
        "docs/foundation/RISK_REGISTER.md": "RISK_REGISTER.template.md",
        "docs/foundation/PROTOTYPE_BRIEF.md": "PROTOTYPE_BRIEF.template.md",
        "docs/foundation/GAME_DESIGN_SPEC.md": "GAME_DESIGN_SPEC.template.md",
        f".agents/skills/{slug}-foundation/SKILL.md": "PROJECT_FOUNDATION_SKILL.template.md",
        ".game-wiki/SCHEMA.md": "WIKI_SCHEMA.template.md",
    }
    for destination, template_name in mapping.items():
        write_file(target / destination, render_template(template_name, replacements), force, created, skipped)

    config = {
        "schema_version": "1.0",
        "project_slug": slug,
        "game_title": game_title,
        "engine": engine,
        "platforms": platforms,
        "genre": genre,
        "created_at": date.today().isoformat(),
        "skill_sequence": [f"{i:02d}" for i in range(19)] + ["90"],
    }
    write_file(
        target / ".game-planner/config.json",
        json.dumps(config, ensure_ascii=False, indent=2),
        force,
        created,
        skipped,
    )

    initial_files = {
        ".game-wiki/index.md": f"# {game_title} Wiki Index\n\n- [Current State](current-state.md)\n- [Timeline](log.md)\n",
        ".game-wiki/log.md": f"# {game_title} Development Log\n\n- {date.today().isoformat()}: GamePlanner bootstrap created.\n",
        ".game-wiki/current-state.md": (
            f"# Current State\n\n- Goal: UNSET\n- Branch: UNSET\n- HEAD SHA: UNSET\n"
            "- Build ID: UNSET\n- Next safe action: Complete the Game Contract.\n- Do not touch: UNSET\n"
        ),
    }
    for destination, content in initial_files.items():
        write_file(target / destination, content, force, created, skipped)

    wiki_dirs = [
        "raw/sessions", "raw/tool-logs", "raw/screenshots", "raw/playtest-notes",
        "project/systems", "decisions", "incidents", "rules", "experiments",
        "playtests", "verifications", "releases", "handoffs", "_archive",
    ]
    for directory in wiki_dirs:
        write_file(target / ".game-wiki" / directory / ".gitkeep", "", force, created, skipped)

    production_dirs = [
        "work-orders", "impacts", "art", "assets", "balance", "implementation",
        "incidents", "data-validation", "verification", "playtests", "releases",
    ]
    for directory in production_dirs:
        write_file(target / "docs/game-planner" / directory / ".gitkeep", "", force, created, skipped)

    return created, skipped


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", default=None)
    parser.add_argument("--engine", default="UNSET")
    parser.add_argument("--platform", action="append", default=[])
    parser.add_argument("--genre", default="UNSET")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)

    if not valid_slug(args.slug):
        print("--slug must use lowercase kebab-case, for example my-game")
        return 2
    title = args.title or args.slug.replace("-", " ").title()
    created, skipped = bootstrap(
        args.target, args.slug, title, args.engine, args.platform, args.genre, args.force
    )
    print(f"GamePlanner bootstrap complete: {len(created)} written, {len(skipped)} skipped")
    for path in created:
        print(f"+ {path.relative_to(args.target.resolve())}")
    if skipped:
        print("Existing files were not overwritten. Use --force only after reviewing them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
