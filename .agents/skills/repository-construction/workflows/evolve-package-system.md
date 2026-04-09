# Evolve Package System

## Purpose

调整当前仓库里的活包集合，让新增包、拆分包、合并包、迁移包和退役包都有明确落点。

## Use When

- 需要把一个新包加入活包集合
- 某个包已经出现拆分信号
- 两个包需要合并
- 某个包开始迁移或退役

## Inputs

- 当前活包集合工件
- 当前活包集合
- 相关包的结构工件

## Steps

1. 先判断这次变化属于新增、拆分、合并、迁移、退役中的哪一种。
2. 根据这次变化更新 `temp/architecture/repository-root/active-packages.json`。
3. 若是拆分、合并或迁移，为相关包补 `migration-notes.md`。
4. 若新包进入活包集合，则为它补 `tree.txt` 与 `structure.json`。
5. 若旧包进入迁移或退役状态，把状态明确写回 `active-packages.json`。
6. 消费者迁移完成后，再把旧包从活包集合中移出。

若本轮变化同时涉及运行时关系抽象重组，再先回看 `temp/architecture/runtime-model.json`，确认相关 `runtime triad`、两侧 `instance package` 和 `minimal business domain package group` 已经同步。

`active-packages.json` 的最小对象如下：

```json
{
  "repository_stage": "forming | expanding | restructuring | stabilizing | shrinking",
  "active_packages": [],
  "migrating_packages": [],
  "retiring_packages": []
}
```

几种常见变化的最小结果如下：

```json
{
  "add_package": {
    "repository_stage": "expanding",
    "active_packages": ["packages/example"],
    "migrating_packages": [],
    "retiring_packages": []
  },
  "start_migration": {
    "repository_stage": "restructuring",
    "active_packages": ["packages/example", "packages/example-v2"],
    "migrating_packages": ["packages/example"],
    "retiring_packages": []
  },
  "finish_retirement": {
    "repository_stage": "shrinking",
    "active_packages": ["packages/example-v2"],
    "migrating_packages": [],
    "retiring_packages": ["packages/example"]
  }
}
```

## Outputs

- 一份更新后的活包集合工件
- 一组与之对应的包结构工件

## Verification

- 活包集合是否已经更新
- `repository_stage` 是否已经同步
- 迁移中的包是否有明确状态
- 退役包是否已经从活包集合中移出
- `active-packages.json` 是否仍然保持四段固定字段

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../docs/package-model.md](../docs/package-model.md)
