#!/usr/bin/env python3
"""List or install selected GamePlanner upstream tools at their pinned commits."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK = REPO_ROOT / "external/UPSTREAMS.lock.json"


def load_upstreams(lock_path: Path) -> list[dict[str, Any]]:
    data = json.loads(lock_path.read_text(encoding="utf-8"))
    upstreams = data.get("upstreams")
    if not isinstance(upstreams, list):
        raise ValueError("lock file does not contain an upstreams array")
    return [item for item in upstreams if isinstance(item, dict)]


def installable(upstream: dict[str, Any]) -> bool:
    repository = upstream.get("repository")
    integration = upstream.get("integration")
    return (
        isinstance(repository, str)
        and "/" in repository
        and not repository.startswith("gist:")
        and integration != "concept-only"
    )


def select_upstreams(
    upstreams: list[dict[str, Any]],
    ids: list[str] | None = None,
    stages: list[str] | None = None,
    all_installable: bool = False,
) -> list[dict[str, Any]]:
    ids_set = set(ids or [])
    stages_set = set(stages or [])
    selected: list[dict[str, Any]] = []
    for item in upstreams:
        if not installable(item):
            continue
        if all_installable or item.get("id") in ids_set or item.get("stage") in stages_set:
            selected.append(item)
    return selected


def run(command: list[str], dry_run: bool) -> None:
    print("$ " + " ".join(command))
    if not dry_run:
        subprocess.run(command, check=True)


def install_one(upstream: dict[str, Any], destination: Path, update: bool, dry_run: bool) -> None:
    upstream_id = str(upstream["id"])
    repository = str(upstream["repository"])
    pinned_ref = str(upstream["ref"])
    target = destination / upstream_id
    clone_url = f"https://github.com/{repository}.git"

    if target.exists() and not (target / ".git").is_dir():
        raise RuntimeError(f"target exists and is not a git repository: {target}")
    if target.exists() and not update:
        raise RuntimeError(f"target already exists: {target}; pass --update to refresh")

    if not target.exists():
        run(["git", "clone", "--filter=blob:none", "--no-checkout", clone_url, str(target)], dry_run)
    run(["git", "-C", str(target), "fetch", "--depth", "1", "origin", pinned_ref], dry_run)
    run(["git", "-C", str(target), "checkout", "--detach", "FETCH_HEAD"], dry_run)
    if not dry_run and len(pinned_ref) == 40:
        actual = subprocess.run(
            ["git", "-C", str(target), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        if actual != pinned_ref:
            raise RuntimeError(f"{upstream_id}: expected {pinned_ref}, got {actual}")
    print(f"installed {upstream_id} at {pinned_ref}")


def print_catalog(upstreams: list[dict[str, Any]]) -> None:
    for item in upstreams:
        marker = "installable" if installable(item) else "reference-only"
        print(
            f"{item.get('stage','??')}  {item.get('id','unknown'):<36} "
            f"{marker:<14} {item.get('ref','')}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--destination", type=Path, default=Path(".game-planner/upstreams"))
    parser.add_argument("--id", action="append", dest="ids", default=[])
    parser.add_argument("--stage", action="append", dest="stages", default=[])
    parser.add_argument("--all", action="store_true", dest="all_installable")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        upstreams = load_upstreams(args.lock)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"failed to read upstream lock: {exc}")
        return 1

    if args.list:
        print_catalog(upstreams)
        return 0

    selected = select_upstreams(upstreams, args.ids, args.stages, args.all_installable)
    if not selected:
        print("no installable upstream selected; use --id, --stage, --all, or --list")
        return 2

    destination = args.destination.resolve()
    if not args.dry_run:
        destination.mkdir(parents=True, exist_ok=True)
    try:
        for upstream in selected:
            install_one(upstream, destination, args.update, args.dry_run)
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"upstream installation failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
