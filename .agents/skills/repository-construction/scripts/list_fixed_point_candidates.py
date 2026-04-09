#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED = {
    ("src", "wrappers", "entry"),
    ("src", "wrappers", "exit"),
    ("src", "business", "exit"),
    ("src", "tests", "exit"),
}


def extract_fixed_point_suffix(path: Path) -> str | None:
    name = path.name
    if "." not in name:
        return None

    stem, suffix = name.rsplit(".", 1)
    if not stem or stem != suffix:
        return None
    return suffix


def parse_variant(raw_variant: str) -> str:
    if ":" not in raw_variant:
        raise SystemExit(f"invalid variant '{raw_variant}', expected language:suffix")

    _language, suffix = (part.strip() for part in raw_variant.split(":", 1))
    if not suffix:
        raise SystemExit(f"invalid variant '{raw_variant}', expected non-empty suffix")
    return suffix


def load_allowed_suffixes(
    raw_variants: list[str],
    structure_json: str | None,
) -> set[str]:
    allowed_suffixes = {parse_variant(raw_variant) for raw_variant in raw_variants}

    if structure_json:
        structure = json.loads(Path(structure_json).read_text(encoding="utf-8"))
        for variant in structure.get("implementation_variants", []):
            suffix = str(variant.get("suffix", "")).strip()
            if suffix:
                allowed_suffixes.add(suffix)

    return allowed_suffixes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--suffix", help="filter by file suffix without dot, for example go or ts")
    parser.add_argument("--zone", choices=["wrappers-entry", "wrappers-exit", "business-exit", "tests-exit"])
    parser.add_argument(
        "--variant",
        action="append",
        default=[],
        help="allowed implementation variant in language:suffix form; may be repeated",
    )
    parser.add_argument(
        "--structure-json",
        help="load allowed implementation variant suffixes from structure.json",
    )
    parser.add_argument(
        "--strict-naming",
        action="store_true",
        help="only return files whose names match <suffix>.<suffix>",
    )
    parser.add_argument(
        "--invalid-naming",
        action="store_true",
        help="only return files under fixed point directories whose names violate <suffix>.<suffix>",
    )
    parser.add_argument(
        "--strict-membership",
        action="store_true",
        help="only return fixed point files whose suffix belongs to the allowed implementation variants",
    )
    parser.add_argument(
        "--invalid-membership",
        action="store_true",
        help="only return fixed point files whose suffix does not belong to the allowed implementation variants",
    )
    args = parser.parse_args()

    if args.strict_naming and args.invalid_naming:
        raise SystemExit("--strict-naming and --invalid-naming cannot be used together")
    if args.strict_membership and args.invalid_membership:
        raise SystemExit("--strict-membership and --invalid-membership cannot be used together")

    allowed_suffixes = load_allowed_suffixes(args.variant, args.structure_json)
    if (args.strict_membership or args.invalid_membership) and not allowed_suffixes:
        raise SystemExit(
            "--strict-membership or --invalid-membership requires --variant and/or --structure-json"
        )

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

        fixed_point_suffix = extract_fixed_point_suffix(path)
        if args.strict_naming and fixed_point_suffix is None:
            continue
        if args.invalid_naming and fixed_point_suffix is not None:
            continue
        if args.invalid_naming and fixed_point_suffix is None:
            print(path.as_posix())
            continue

        if fixed_point_suffix is None and (args.strict_membership or args.invalid_membership):
            if args.invalid_membership:
                print(path.as_posix())
            continue

        if args.strict_membership and fixed_point_suffix not in allowed_suffixes:
            continue
        if args.invalid_membership and fixed_point_suffix in allowed_suffixes:
            continue

        print(path.as_posix())


if __name__ == "__main__":
    main()
