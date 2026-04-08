#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def to_title(skill_dir: str) -> str:
    return " ".join(part.capitalize() for part in skill_dir.split("-"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir")
    parser.add_argument("description")
    parser.add_argument("--skills-root", default=".agents/skills")
    parser.add_argument("--with-docs", action="store_true")
    parser.add_argument("--with-scripts", action="store_true")
    args = parser.parse_args()

    root = Path(args.skills_root) / args.skill_dir
    (root / "references").mkdir(parents=True, exist_ok=True)
    (root / "workflows").mkdir(parents=True, exist_ok=True)
    if args.with_docs:
        (root / "docs").mkdir(parents=True, exist_ok=True)
    if args.with_scripts:
        (root / "scripts").mkdir(parents=True, exist_ok=True)

    workflow_name = "WORKFLOW.md"
    write(
        root / "SKILL.md",
        "\n".join(
            [
                "---",
                f"name: {args.skill_dir}",
                f"description: {args.description}",
                "---",
                "",
                f"# {to_title(args.skill_dir)}",
                "",
                "补充场景引入、对象边界、最短路径和文件导航。",
                "",
                "## 文件导航",
                "",
                "- [references/REFERENCE.md](references/REFERENCE.md)",
                f"- [workflows/{workflow_name}](workflows/{workflow_name})",
                "",
            ]
        ),
    )
    write(root / "references" / "REFERENCE.md", "# Reference\n")
    write(
        root / "workflows" / workflow_name,
        "\n".join(
            [
                "# Workflow",
                "",
                "## Purpose",
                "",
                "补充任务路径、步骤和核对方式。",
                "",
            ]
        ),
    )
    print(root.as_posix())


if __name__ == "__main__":
    main()
