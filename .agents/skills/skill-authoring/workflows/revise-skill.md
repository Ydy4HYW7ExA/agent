# Revise Skill

## Purpose

重构一个已经存在但入口变弱、结构失焦、文件互相抢职责的 skill。

## Use When

- `SKILL.md` 已经不能承担总入口
- 文件之间缺少稳定回链
- reference、workflow 和 doc 开始互相吞并

## Inputs

- 当前 skill 目录
- 文件职责判断

## Steps

1. 先判断当前 skill 的问题属于“最小结构失真”还是“最小可用状态失真”。
2. 先修 `SKILL.md`，让它稳定承担入口。
3. 把静态真值回收进 `references/`，把任务路径回收进 `workflows/`。
4. 合并那些只有姿态、没有独立信息量的薄文件。
5. 删除没有对象支撑的空附属面。
6. 回看首现术语是否都在第一次出现时给出了定义。

## Outputs

- 一个收束后的 skill

## Verification

- 文件职责是否已经分开
- 读者是否能从 `SKILL.md` 走完整个 skill
- 是否还残留只有目录感、没有对象感的文件
- 首现术语是否还在定义前先跑出来

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../docs/skill-system.md](../docs/skill-system.md)
