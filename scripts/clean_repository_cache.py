#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


CACHE_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
}

CACHE_FILE_SUFFIXES = {
    ".pyc",
    ".pyo",
}


def collect_cache_paths(root: Path) -> list[Path]:
    matches: set[Path] = set()

    for path in root.rglob("*"):
        if path.is_dir() and path.name in CACHE_DIR_NAMES:
            matches.add(path)
            continue
        if path.is_file() and path.suffix in CACHE_FILE_SUFFIXES:
            matches.add(path)

    selected: list[Path] = []
    for path in sorted(matches, key=lambda candidate: (len(candidate.parts), candidate.as_posix())):
        if any(parent in selected for parent in path.parents):
            continue
        selected.append(path)

    return selected


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
        return
    path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"missing root: {root}", file=sys.stderr)
        return 1

    cache_paths = collect_cache_paths(root)
    if not cache_paths:
        print("no cache paths found")
        return 0

    for path in cache_paths:
        action = "would remove" if args.dry_run else "removed"
        print(f"{action}: {path.relative_to(root).as_posix()}")
        if not args.dry_run:
            remove_path(path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
