# Shape Task Path

## Purpose

把清洗后的表达收成任务入口，让后续工作不再依赖聊天材料本身。

## Use When

- 对象和边界已经稳定
- 当前需要开始执行
- 一个问题已经拆出多个动作，但还没排出路径

## Inputs

- `clean expression`
- 已确定的 skill 去向

## Steps

1. 按对象和动作切出任务项，不按聊天顺序切。
2. 每项任务都补上边界、下一跳和预期工件。
3. 若某项还只能停留在分析材料，移入目标仓库的草稿工件，不冒充正式任务。
4. 删除所有不能直接推动执行的聊天残留。

## Outputs

- 一条或多条 `task path`

## Verification

- 每项任务是否都含对象、动作、边界、下一跳和预期工件
- 后续执行是否还需要回头阅读整段聊天
- 任务路径是否已经能直接挂到 workflow

## Related

- [../references/TERMINOLOGY.md](../references/TERMINOLOGY.md)
- [../../documentation-authoring/references/DRAFT-ARTIFACTS.md](../../documentation-authoring/references/DRAFT-ARTIFACTS.md)
