---
name: repository-construction
description: 立即启用：当任务已经进入仓库建设对象本身，需要从问题边界一直落到仓库根、包根、文件关系、注释、文档和脚本边界。
---

# Repository Construction

“建设一个仓库”这句话里通常混着很多不同动作：定对象、拆结构、写代码、补注释、写文档、做脚本。它们表面上属于不同面，实际却不断指向同一组边界判断。包为什么会出现，包为什么是独立工作范围，包为什么有统一语言，封装区为什么会出现，为什么只保留 `entry` 与 `exit` 这两类固定出入口，为什么一个包允许多个语言变体并列存在，仓库根和包根为什么都不能只停留在概念句上，这些问题最后都回到同一条建设链上。

这里先把几个关键对象摆出来。`protocol` 指一类稳定交互的契约对象；`client kernel` 指消费这类契约的一侧内核；`server kernel` 指提供这类契约的一侧内核；`instance package` 指把若干内核装配成可运行实例的包对象；`bounded context`、`package root`、`package language`、`entry file`、`exit file` 与 `implementation variant` 则继续把这些对象落成仓库根、包根、固定出入口集合、自由内部实现和文件关系。再往后，编码、注释、文档和脚本边界才有真实着力点。

## 最短路径

1. 先读 [workflows/shape-repository-task.md](workflows/shape-repository-task.md)
2. 需要从运行关系继续推到协议、内核和实例包时，读 [workflows/model-runtime-structure.md](workflows/model-runtime-structure.md)
3. 需要判断包是否出现以及包结构怎么落时，读 [workflows/create-package.md](workflows/create-package.md)
4. 需要核对文件关系时，读 [workflows/inspect-relations.md](workflows/inspect-relations.md)
5. 需要调整活包集合和迁移状态时，读 [workflows/evolve-package-system.md](workflows/evolve-package-system.md)
6. 需要补“为什么会推出这些对象与边界”时，读 [docs/repository-derivation.md](docs/repository-derivation.md)、[docs/package-model.md](docs/package-model.md) 和 [docs/package-system-evolution.md](docs/package-system-evolution.md)

## 文件导航

- [references/REFERENCE.md](references/REFERENCE.md)
- [references/TERMINOLOGY.md](references/TERMINOLOGY.md)
- [references/STRUCTURE.md](references/STRUCTURE.md)
- [references/DECISIONS.md](references/DECISIONS.md)
- [references/LIFECYCLE.md](references/LIFECYCLE.md)
- [references/RELATIONS.md](references/RELATIONS.md)
- [workflows/shape-repository-task.md](workflows/shape-repository-task.md)
- [workflows/model-runtime-structure.md](workflows/model-runtime-structure.md)
- [workflows/create-package.md](workflows/create-package.md)
- [workflows/inspect-relations.md](workflows/inspect-relations.md)
- [workflows/evolve-package-system.md](workflows/evolve-package-system.md)
- [docs/repository-derivation.md](docs/repository-derivation.md)
- [docs/package-model.md](docs/package-model.md)
- [docs/package-system-evolution.md](docs/package-system-evolution.md)
- [scripts/create_package_scaffold.py](scripts/create_package_scaffold.py)
- [scripts/list_fixed_point_candidates.py](scripts/list_fixed_point_candidates.py)

## 使用约束

- 先建对象关系，再下结构结论
- 所有“是否出现”问题都按显式决策处理
- 仓库根和包根都必须写成显式结构工件
- 脚手架只承接确定性建骨架，不替代对象判断
- 根 `scripts/` 不承接这里的方法脚本
