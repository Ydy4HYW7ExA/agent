# Model Runtime Structure

## Purpose

把运行中的依赖关系收成可以继续落到仓库结构的稳定表达。

## Use When

- 需要描述某个实例如何消费另一个实例的能力
- 需要从运行关系继续推到协议、内核和实例包
- 需要明确这些中间对象之后落到哪里

## Inputs

- 上下游实例
- 交互语义
- 当前已有协议或内核

## Steps

1. 先把关系写成过程边：`consumer instance -> provider instance`。
2. 判断这条边是否需要新的 `protocol`，还是复用已有协议。
3. 为消费侧补 `client kernel`，为提供侧补 `server kernel`。
4. 判断这些内核是否已经形成 `instance package` 的稳定装配对象。
5. 决定当前阶段的落点：分析草稿、目标仓库文档，或代码对象。
6. 把本轮分析结果写入目标仓库 `temp/architecture/runtime-model.json`，避免对象只停留在正文句子里。
7. 让 `runtime-model.json` 至少包含：上下游实例、协议、两侧内核、实例包、当前落点。
8. 若当前轮的分析会影响活包集合，再把结论继续写回 `temp/architecture/repository-root/active-packages.json` 或交给 [evolve-package-system.md](evolve-package-system.md)。

## Outputs

- 一条稳定的运行关系表达
- 一组中间对象及其当前落点
- 一份 `temp/architecture/runtime-model.json`

## Verification

- 是否已经把过程边与构成对象分开
- 是否显式写出了协议与两侧内核
- 是否已经说明这些对象当前落在哪里
- 当前落点是否已经写进 `runtime-model.json`

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../references/TERMINOLOGY.md](../references/TERMINOLOGY.md)
- [../docs/repository-derivation.md](../docs/repository-derivation.md)
