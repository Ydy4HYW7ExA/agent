# Model Runtime Structure

## Purpose

把运行中的实例关系和构成关系拆开，收成可以继续落到仓库结构的稳定表达。

## Use When

- 需要描述某个实例如何消费另一个实例的能力
- 需要从运行关系继续推到协议、三元和两侧实例包
- 需要明确这些中间对象之后落到哪里

## Inputs

- 上下游实例
- 交互语义
- 当前已有协议或内核

## Steps

1. 先把关系写成过程边：`consumer instance -> provider instance`。
2. 把这条边上的依赖写成 `process dependency`，明确它是关于实例的依赖，不直接承担构成判断。
3. 判断这条边是否需要新的 `protocol`，还是复用已有协议。
4. 为消费侧补 `client kernel`，为提供侧补 `server kernel`。
5. 把 `protocol`、`client kernel` 与 `server kernel` 收成一份 `runtime triad`，并明确写下它只是关系抽象，不是实例。
6. 再分别判断消费侧和提供侧是否已经形成稳定的 `consumer instance package` 与 `provider instance package`。
7. 若一份 `runtime triad` 与两侧 `instance package` 都已明确，把它们收成一份 `minimal business domain package group`。
8. 决定当前阶段的落点：分析草稿、目标仓库文档，或代码对象。
9. 把本轮分析结果写入目标仓库 `temp/architecture/runtime-model.json`，避免对象只停留在正文句子里。
10. 让 `runtime-model.json` 至少包含：上下游实例、过程性依赖、三元、两侧实例包、最小业务域包群、当前落点。
11. 若当前轮的分析会影响活包集合，再把结论继续写回 `temp/architecture/repository-root/active-packages.json` 或交给 [evolve-package-system.md](evolve-package-system.md)。

## Outputs

- 一条稳定的运行关系表达
- 一组被拆开的构成对象与实例对象
- 一份 `temp/architecture/runtime-model.json`

## Verification

- 是否已经把过程边、过程性依赖与构成对象分开
- 是否显式写出了协议、两侧内核和三元
- 是否已经显式写出消费侧与提供侧实例包
- 三元是否没有被写成实例对象
- 是否已经说明这些对象当前落在哪里
- 当前落点是否已经写进 `runtime-model.json`

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../references/TERMINOLOGY.md](../references/TERMINOLOGY.md)
- [../docs/repository-derivation.md](../docs/repository-derivation.md)
