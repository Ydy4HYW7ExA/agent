# Shape Repository Task

## Purpose

把已经清洗过的问题表达收成仓库建设任务入口，并决定先走哪条对象路径。

## Use When

- 当前问题已经进入仓库建设
- 一个问题同时涉及结构、文档或脚本边界
- 需要安排判断顺序

## Inputs

- 清洗后的表达
- 当前已知对象和边界

## Steps

1. 先判断问题首先落在运行时建模、包判断、包结构、文件关系、仓库根工件、文档落点还是脚本边界。
2. 若同时覆盖多个面，按 [../references/STRUCTURE.md](../references/STRUCTURE.md) 的主链排序。
3. 若问题已经涉及 `compositional dependency`、`process dependency`、`protocol`、`client kernel`、`server kernel`、`runtime triad`、`instance package` 或 `minimal business domain package group`，把它继续挂到 [model-runtime-structure.md](model-runtime-structure.md)。
4. 若问题已经涉及仓库根结构或包体系状态，把 `temp/architecture/repository-root/tree.txt`、`structure.json` 与 `active-packages.json` 同时列入本轮工件清单。
5. 为每项任务挂上后续 workflow。
6. 把当前仍缺的事实显式列出；若事实尚未稳定，先落进目标仓库 `temp/` 草稿工件。
7. 记录每项任务的预期工件，不让任务只剩动作没有产物。

## Outputs

- 一组仓库建设任务项

## Verification

- 每项任务是否都能指出对象、动作和边界
- 每项任务是否已经指出预期工件
- 顺序是否符合推导链
- 任务是否已经脱离泛泛讨论
- 若问题涉及运行时对象，是否已经进入 `model-runtime-structure.md`
- 若问题涉及仓库根，仓库根三份工件是否都已经被纳入本轮任务项

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../../documentation-authoring/references/DRAFT-ARTIFACTS.md](../../documentation-authoring/references/DRAFT-ARTIFACTS.md)
