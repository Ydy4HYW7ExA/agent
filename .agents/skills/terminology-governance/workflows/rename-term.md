# Rename Term

## Purpose

把已经误导结构的旧词退场，并让新词接管入口。

## Use When

- 旧词已经造成边界混乱
- 新词已经稳定
- 关键入口需要完成一轮迁移

## Inputs

- 旧词
- 新词
- 受影响文件

## Steps

1. 在术语表里把旧词降格为 `deprecated term` 或 `alias`。
2. 使用 [../references/LOCAL-TERM-TABLE.md](../references/LOCAL-TERM-TABLE.md) 中的记录格式写清迁移关系。
3. 先改共享入口，再改局部入口，再改解释和例子。
4. 回看关键入口，确认不会再让读者猜“这两个词是不是同一个对象”。

## Outputs

- 一轮完成的术语迁移

## Verification

- 关键入口是否还残留旧主词
- 历史词是否已经退到正确位置
- 新词是否已经接管主表述

## Related

- [../references/LOCAL-TERM-TABLE.md](../references/LOCAL-TERM-TABLE.md)
- [../docs/term-governance.md](../docs/term-governance.md)
