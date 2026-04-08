#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


EXPECTED = {
    ("src", "wrappers", "entry"),
    ("src", "wrappers", "exit"),
    ("src", "business", "exit"),
    ("src", "tests", "exit"),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--suffix", help="filter by file suffix without dot, for example go or ts")
    parser.add_argument("--zone", choices=["wrappers-entry", "wrappers-exit", "business-exit", "tests-exit"])
    args = parser.parse_args()

    root = Path(args.root)

    expected = EXPECTED
    if args.zone:
        mapping = {
            "wrappers-entry": {("src", "wrappers", "entry")},
            "wrappers-exit": {("src", "wrappers", "exit")},
            "business-exit": {("src", "business", "exit")},
            "tests-exit": {("src", "tests", "exit")},
        }
        expected = mapping[args.zone]

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative_parts = path.relative_to(root).parts
        if len(relative_parts) < 4:
            continue

        segment = tuple(relative_parts[:3])
        if segment not in expected:
            continue

        if args.suffix and path.suffix != f".{args.suffix}":
            continue

        print(path.as_posix())


if __name__ == "__main__":
    main()
