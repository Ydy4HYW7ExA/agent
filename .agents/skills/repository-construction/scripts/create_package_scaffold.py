#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


PACKAGE_COLLECTION_DIR_NAMES = {
    "packages",
    "package",
    "modules",
    "module",
    "services",
    "service",
    "apps",
    "app",
}


def touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("", encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def validate_suffix(suffix: str) -> str:
    if not suffix:
        raise SystemExit("variant suffix must not be empty")
    if suffix.strip() != suffix:
        raise SystemExit(f"invalid variant suffix '{suffix}', surrounding whitespace is not allowed")
    if "." in suffix:
        raise SystemExit(f"invalid variant suffix '{suffix}', dot is not allowed")
    if "/" in suffix or "\\" in suffix:
        raise SystemExit(f"invalid variant suffix '{suffix}', path separator is not allowed")
    return suffix


def parse_variants(raw_variants: list[str]) -> list[dict[str, str]]:
    variants: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()
    seen_suffixes: set[str] = set()
    for raw in raw_variants:
        if ":" not in raw:
            raise SystemExit(f"invalid variant '{raw}', expected language:suffix")
        language, suffix = (part.strip() for part in raw.split(":", 1))
        if not language:
            raise SystemExit(f"invalid variant '{raw}', expected non-empty language")
        suffix = validate_suffix(suffix)

        pair_key = (language, suffix)
        if pair_key in seen_pairs:
            raise SystemExit(f"duplicate variant '{raw}'")
        if suffix in seen_suffixes:
            raise SystemExit(
                f"duplicate variant suffix '{suffix}', fixed point file names would collide"
            )

        seen_pairs.add(pair_key)
        seen_suffixes.add(suffix)
        variants.append({"language": language, "suffix": suffix})

    if not variants:
        raise SystemExit("at least one --variant is required")
    return variants


def require_non_empty(name: str, values: list[str]) -> list[str]:
    normalized = [value.strip() for value in values if value.strip()]
    if not normalized:
        raise SystemExit(f"{name} must not be empty")
    return normalized


def infer_repository_root(package_root: Path) -> Path:
    if package_root.parent.name in PACKAGE_COLLECTION_DIR_NAMES:
        return package_root.parent.parent
    return package_root.parent


def resolve_repository_root(package_root: Path, raw_repository_root: str | None) -> Path:
    if raw_repository_root:
        return Path(raw_repository_root).resolve()
    return infer_repository_root(package_root)


def resolve_artifact_root(repository_root: Path, raw_artifacts_root: str) -> Path:
    path = Path(raw_artifacts_root)
    if path.is_absolute():
        return path
    return (repository_root / path).resolve()


def relativize(path: Path, root: Path, label: str) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as exc:
        raise SystemExit(f"{label} must stay inside repository root {root.as_posix()}") from exc


def render_zone(
    lines: list[str],
    prefix: str,
    name: str,
    with_entry: bool,
    files: dict[str, list[str]],
    is_last: bool,
) -> None:
    branch = "└──" if is_last else "├──"
    lines.append(f"{prefix}{branch} {name}/")
    zone_prefix = f"{prefix}{'    ' if is_last else '│   '}"

    children: list[tuple[str, list[str]]] = []
    if with_entry:
        children.append(("entry/", files.get("entry", [])))
    children.append(("exit/", files.get("exit", [])))
    children.append(("...", []))

    for index, (child_name, child_files) in enumerate(children):
        child_is_last = index == len(children) - 1
        child_branch = "└──" if child_is_last else "├──"
        lines.append(f"{zone_prefix}{child_branch} {child_name}")
        if child_files:
            file_prefix = f"{zone_prefix}{'    ' if child_is_last else '│   '}"
            for file_index, child_file in enumerate(child_files):
                file_branch = "└──" if file_index == len(child_files) - 1 else "├──"
                lines.append(f"{file_prefix}{file_branch} {child_file}")


def render_tree(
    package_name: str,
    with_wrappers: bool,
    with_tests: bool,
    optional_surfaces: list[str],
    fixed_point_sets: dict[str, dict[str, list[str]]],
) -> str:
    top_level = ["config/", "src/"] + optional_surfaces
    lines = [f"{package_name}/"]

    for index, name in enumerate(top_level):
        is_last = index == len(top_level) - 1
        branch = "└──" if is_last else "├──"
        lines.append(f"{branch} {name}")

        if name == "config/":
            config_prefix = "    " if is_last else "│   "
            config_children = ["business/"]
            if with_wrappers:
                config_children.append("wrappers/")
            if with_tests:
                config_children.append("tests/")
            for child_index, child in enumerate(config_children):
                child_branch = "└──" if child_index == len(config_children) - 1 else "├──"
                lines.append(f"{config_prefix}{child_branch} {child}")
            continue

        if name == "src/":
            src_prefix = "    " if is_last else "│   "
            zones: list[tuple[str, bool, dict[str, list[str]]]] = []
            if with_wrappers:
                zones.append(("wrappers", True, fixed_point_sets.get("wrappers", {})))
            zones.append(("business", False, fixed_point_sets.get("business", {})))
            if with_tests:
                zones.append(("tests", False, fixed_point_sets.get("tests", {})))
            for zone_index, (zone_name, with_entry, zone_files) in enumerate(zones):
                render_zone(lines, src_prefix, zone_name, with_entry, zone_files, zone_index == len(zones) - 1)

    return "\n".join(lines) + "\n"


def build_structure(
    package_root: str,
    package_name: str,
    package_language: list[str],
    implementation_variants: list[dict[str, str]],
    translation_upstream: list[str],
    translation_goal: str | None,
    with_wrappers: bool,
    with_tests: bool,
    optional_surfaces: list[str],
    fixed_point_sets: dict[str, dict[str, list[str]]],
) -> dict[str, object]:
    structure: dict[str, object] = {
        "package_root": package_root,
        "package_language": package_language,
        "implementation_variants": implementation_variants,
        "with_wrappers": with_wrappers,
        "with_tests": with_tests,
        "fixed_point_sets": fixed_point_sets,
        "optional_surfaces": optional_surfaces,
    }

    if with_wrappers:
        structure["translation_boundary"] = {
            "exists": True,
            "upstream": translation_upstream,
            "goal": translation_goal,
        }

    if len(implementation_variants) > 1:
        structure["equivalence_contract_artifact"] = f"temp/packages/{package_name}/equivalence.md"

    return structure


def build_fixed_point_file_names(implementation_variants: list[dict[str, str]]) -> list[str]:
    return [f"{variant['suffix']}.{variant['suffix']}" for variant in implementation_variants]


def create_fixed_point_files(
    root: Path,
    base: Path,
    implementation_variants: list[dict[str, str]],
) -> list[str]:
    relative_paths: list[str] = []
    for file_name in build_fixed_point_file_names(implementation_variants):
        touch(base / file_name)
        relative_paths.append(base.joinpath(file_name).relative_to(root).as_posix())
    return relative_paths


def write_artifacts(
    artifact_root: Path,
    package_name: str,
    package_language: list[str],
    implementation_variants: list[dict[str, str]],
    translation_upstream: list[str],
    translation_goal: str | None,
    with_wrappers: bool,
    with_tests: bool,
    optional_surfaces: list[str],
    fixed_point_sets: dict[str, dict[str, list[str]]],
    package_root: str,
) -> None:
    package_artifact_root = artifact_root / package_name
    write(
        package_artifact_root / "tree.txt",
        render_tree(
            package_name,
            with_wrappers,
            with_tests,
            optional_surfaces,
            fixed_point_sets,
        ),
    )
    write(
        package_artifact_root / "structure.json",
        json.dumps(
            build_structure(
                package_root=package_root,
                package_name=package_name,
                package_language=package_language,
                implementation_variants=implementation_variants,
                translation_upstream=translation_upstream,
                translation_goal=translation_goal,
                with_wrappers=with_wrappers,
                with_tests=with_tests,
                optional_surfaces=optional_surfaces,
                fixed_point_sets=fixed_point_sets,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )
    if len(implementation_variants) > 1:
        write(
            package_artifact_root / "equivalence.md",
            "\n".join(
                [
                    "# Equivalence Contract",
                    "",
                    "当前等价实现变体如下：",
                    "",
                    *[f"- `{variant['language']}` -> `{variant['suffix']}.{variant['suffix']}`" for variant in implementation_variants],
                    "",
                    "继续补齐下面三项：",
                    "",
                    "1. 这些变体共享的固定点职责。",
                    "2. 当前仍未对齐的公开行为。",
                    "3. 需要哪组 `conformance suite` 继续核对一致性。",
                    "",
                ]
            ),
        )
    write(
        package_artifact_root / "scaffold-notes.md",
        "\n".join(
            [
                "# Scaffold Notes",
                "",
                "这个脚手架只完成确定性目录和第一份结构工件，不替代包边界判断。",
                "",
                "固定点文件已经按 `<suffix>.<suffix>` 自动生成。",
                "",
                "后续至少补齐下面几项：",
                "",
                "1. 补问题边界、统一语言和语义区出现原因这三句自然语言说明。",
                "2. 按 `docs/package-model.md` 的最小内容样板补到出入口文件。",
                "3. 若存在多个 `implementation_variants`，继续写实 `equivalence.md`。",
                "4. 若包已经承接活需求，再把它写入 `temp/architecture/repository-root/active-packages.json`。",
                "",
            ]
        )
        + "\n",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("package_root")
    parser.add_argument("--variant", action="append", default=[], help="language:suffix")
    parser.add_argument("--repository-root")
    parser.add_argument("--with-wrappers", action="store_true")
    parser.add_argument("--with-tests", action="store_true")
    parser.add_argument("--package-language", nargs="*", default=[])
    parser.add_argument("--translation-upstream", nargs="*", default=[])
    parser.add_argument("--translation-goal")
    parser.add_argument("--artifacts-root", default="temp/packages")
    parser.add_argument("--with-docs", action="store_true")
    parser.add_argument("--with-scripts", action="store_true")
    parser.add_argument("--with-fixtures", action="store_true")
    parser.add_argument("--with-temp", action="store_true")
    args = parser.parse_args()

    root = Path(args.package_root).resolve()
    repository_root = resolve_repository_root(root, args.repository_root)
    if repository_root == root:
        raise SystemExit("repository root must be higher than package_root")

    package_root_for_structure = relativize(root, repository_root, "package_root")
    artifact_root = resolve_artifact_root(repository_root, args.artifacts_root)
    variants = parse_variants(args.variant)
    package_language = require_non_empty("package_language", args.package_language)

    (root / "config" / "business").mkdir(parents=True, exist_ok=True)
    (root / "src" / "business" / "exit").mkdir(parents=True, exist_ok=True)

    fixed_point_sets: dict[str, dict[str, list[str]]] = {
        "business": {
            "exit": create_fixed_point_files(root, root / "src" / "business" / "exit", variants)
        }
    }

    translation_upstream: list[str] = []
    translation_goal: str | None = None
    if args.with_wrappers:
        translation_upstream = require_non_empty("translation_upstream", args.translation_upstream)
        translation_goal = (args.translation_goal or "").strip()
        if not translation_goal:
            raise SystemExit("--translation-goal is required when --with-wrappers is set")
        (root / "config" / "wrappers").mkdir(parents=True, exist_ok=True)
        (root / "src" / "wrappers" / "entry").mkdir(parents=True, exist_ok=True)
        (root / "src" / "wrappers" / "exit").mkdir(parents=True, exist_ok=True)
        fixed_point_sets["wrappers"] = {
            "entry": create_fixed_point_files(root, root / "src" / "wrappers" / "entry", variants),
            "exit": create_fixed_point_files(root, root / "src" / "wrappers" / "exit", variants),
        }

    if args.with_tests:
        (root / "config" / "tests").mkdir(parents=True, exist_ok=True)
        (root / "src" / "tests" / "exit").mkdir(parents=True, exist_ok=True)
        fixed_point_sets["tests"] = {
            "exit": create_fixed_point_files(root, root / "src" / "tests" / "exit", variants)
        }

    for flag, name in (
        (args.with_docs, "docs"),
        (args.with_scripts, "scripts"),
        (args.with_fixtures, "fixtures"),
        (args.with_temp, "temp"),
    ):
        if flag:
            (root / name).mkdir(parents=True, exist_ok=True)

    optional_surfaces = [
        f"{name}/"
        for enabled, name in (
            (args.with_docs, "docs"),
            (args.with_scripts, "scripts"),
            (args.with_fixtures, "fixtures"),
            (args.with_temp, "temp"),
        )
        if enabled
    ]

    write_artifacts(
        artifact_root=artifact_root,
        package_name=root.name,
        package_language=package_language,
        implementation_variants=variants,
        translation_upstream=translation_upstream,
        translation_goal=translation_goal,
        with_wrappers=args.with_wrappers,
        with_tests=args.with_tests,
        optional_surfaces=optional_surfaces,
        fixed_point_sets=fixed_point_sets,
        package_root=package_root_for_structure,
    )

    print(root.as_posix())


if __name__ == "__main__":
    main()
