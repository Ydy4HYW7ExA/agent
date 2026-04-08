# Place Information

## Purpose

决定一条信息应落在哪个文档面。

## Use When

- 已经知道要写什么
- 还没确定该写进哪里
- 需要避免同一条知识在多个地方重复长出

## Inputs

- 待写信息
- 服务对象
- 预期读者

## Steps

1. 判断这条信息属于方法、仓库事实、局部实现意图，还是临时分析材料。
2. 方法落 skill，事实落仓库文档，局部意图落注释，临时分析材料落草稿工件。
3. 若这条信息里首次引入了术语，先补定义，再决定落点。
4. 若落草稿，则同时写明作用域、升级条件和退出条件。
5. 为目标文档补回链，防止知识再次游离。

## Outputs

- 一个明确的信息落点

## Verification

- 是否只有一个主落点
- 新术语是否已经先定义后使用
- 草稿是否被误写成正式真值
- 读者是否能在正确位置找到这条知识

## Related

- [../references/WRITING.md](../references/WRITING.md)
- [../references/DRAFT-ARTIFACTS.md](../references/DRAFT-ARTIFACTS.md)
