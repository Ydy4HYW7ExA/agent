# Inspect Relations

## Purpose

核对包内文件关系是否合法。

## Use When

- 包结构新增或重构之后
- 需要判断是否绕开固定出入口
- 需要检查包是否开始出现拆分信号

## Inputs

- 目标包
- 固定出入口候选文件
- 直接相连的实现文件

## Steps

1. 先列出固定出入口候选路径，可借助 [../scripts/list_fixed_point_candidates.py](../scripts/list_fixed_point_candidates.py) 枚举 `wrappers/entry`、`wrappers/exit`、`business/exit`、`tests/exit` 位置。需要先筛命名时，使用 `--strict-naming`；需要继续筛 `suffix` 是否属于当前包的 `implementation_variants` 时，再补 `--structure-json` 或显式 `--variant` 配合 `--strict-membership`。
2. 再做人工确认：固定点文件必须写成 `<suffix>.<suffix>`，并且这个 `suffix` 必须出现在当前包的 `implementation_variants` 中。
3. 从每个固定出入口文件出发，人工查看一跳语法依赖：`import`、`require`、`use`、显式注册表或显式装配表；当前不建立依赖关系检测脚本。
4. 若语言或框架会通过配置、注册表或运行时装配间接连线，则把这些显式配置文件也纳入“一跳实现文件”范围。
5. 检查四类风险：`wrappers/entry` 回头依赖 `wrappers` 内部文件、`wrappers/exit` 碰 `wrappers/entry` 或区外源码、`business/exit` 碰 `business` 区外源码、某个 `business/exit` 直接依赖多个 `business` 非出口文件。
6. 将结论落到“通过”“结构异常”或“拆分信号”。

最小结论对象可以写成：

```json
{
  "package_root": "",
  "status": "pass | structural_violation | split_signal",
  "checked_files": [],
  "notes": []
}
```

两种典型结论如下：

```json
{
  "package_root": "packages/example",
  "status": "pass",
  "checked_files": [
    "src/wrappers/entry/py.py",
    "src/wrappers/exit/py.py",
    "src/business/exit/py.py"
  ],
  "notes": [
    "no forbidden direct dependency found"
  ]
}
```

```json
{
  "package_root": "packages/example",
  "status": "structural_violation",
  "checked_files": [
    "src/wrappers/exit/py.py"
  ],
  "notes": [
    "wrappers exit depends on src/business/internal/pool.py"
  ]
}
```

## Outputs

- 一份文件级关系核对结果

## Verification

- 是否基于真实文件而不是目录想象下结论
- 候选路径是否经过了人工确认
- 固定点文件名是否合法，且是否已经通过结构工件或显式 variant 集合与当前 `implementation_variants` 对齐
- 是否没有把人工判断冒充成自动检测结果
- “直接相连”是否只覆盖固定出入口的一跳关系及其显式装配文件
- 若结论是拆分信号，是否已经说明它对应的是哪一个 `business/exit` 文件写散

## Related

- [../references/RELATIONS.md](../references/RELATIONS.md)
- [../references/DECISIONS.md](../references/DECISIONS.md)
