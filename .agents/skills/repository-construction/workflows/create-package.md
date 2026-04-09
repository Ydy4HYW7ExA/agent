# Create Package

## Purpose

为一个已经确认成立的包根建立最小可用结构。

## Use When

- 包根判断已经成立
- 需要把边界真正落成结构

## Inputs

- 包根路径
- 当前包统一语言
- `implementation_variants`
- 是否存在构成性上游依赖
- 是否需要 `wrappers` 语义区
- 是否需要 `tests` 语义区
- 当前需要出现的附属面

## Steps

1. 先明确这次建包的运行时决策对象，至少写出 `implementation_variants`、`with_wrappers`、`with_tests`、`package_language` 和 `fixed_point_sets`。
2. 若存在构成性上游依赖，则补一份 `translation boundary object`；若不存在，则明确记录 `with_wrappers=false`。
3. 建立 `config/` 与 `src/` 的核心结构。
4. 在 `src/` 下只建立固定出入口目录：`wrappers/entry`、`wrappers/exit`、`business/exit`、`tests/exit`。其余源码文件按自由内部实现处理，结构里只保留这两类固定目录。
5. 每个固定点目录都按 `implementation_variants[*].suffix` 自动生成 `<suffix>.<suffix>` 文件。固定点语义由目录承接，文件名不再承接额外业务语义。
6. 如需加速建骨架，可运行 [../scripts/create_package_scaffold.py](../scripts/create_package_scaffold.py)；脚本要求显式传入 `package_language`、`implementation_variants` 以及必要的结构 flag。若出现 `wrappers`，还要显式传入 `translation_upstream` 与 `translation_goal`。脚本不再接收任意固定点文件名集合，而是按 `suffix` 自动生成固定点文件。
7. 脚本默认把工件写到目标仓库自己的 `temp/packages/<package-name>/`。若 `package_root` 不是常见的包集合子路径，显式传入 `--repository-root`，不要让工件相对当前执行目录漂走。
8. 核对第一份结构工件是否已经写实。至少检查：`package_language`、`implementation_variants`、`fixed_point_sets` 已经明确；若出现 `wrappers`，再检查 `translation_boundary.goal`；`optional_surfaces` 只要求显式，不要求非空。
9. 若存在多个 `implementation_variants`，脚手架应同时写出 `equivalence.md`；随后立刻把等价职责和一致性核对方式补实，避免多变体并列只停留在文件名层。
10. 若脚手架已经生成了出入口文件，立刻按 [../docs/package-model.md](../docs/package-model.md) 里的最小内容样板补到对应位置，避免结构只剩空文件。
11. 新包若已经承接活需求，立刻进入 [evolve-package-system.md](evolve-package-system.md)，把它写进 `temp/architecture/repository-root/active-packages.json`。

## Outputs

- 一个最小可用的新包骨架
- 一份显式的包结构工件

## Verification

- 这次结构是否由显式运行时决策驱动
- `wrappers` 是否只在存在构成性上游依赖时出现
- 固定出入口目录是否齐全且命名正确
- 固定点文件是否全部采用 `<suffix>.<suffix>` 命名
- 第一份结构工件是否已经落到草稿区
- `tree.txt` 与 `structure.json` 是否都已经生成
- 若出现 `wrappers`，`translation_boundary.goal` 是否已写实
- 多变体并列时，是否已经出现 `equivalence contract` 草稿

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../references/DECISIONS.md](../references/DECISIONS.md)
- [../docs/package-model.md](../docs/package-model.md)
- [../../documentation-authoring/references/DRAFT-ARTIFACTS.md](../../documentation-authoring/references/DRAFT-ARTIFACTS.md)
