# Create Skill

## Purpose

从零建立一个新的 skill，并让它一开始就拥有清楚的入口和结构。

## Use When

- 某个能力边界已经稳定到值得独立存在
- 现有 skill 无法自然扩展承接它
- 需要让读者反复进入同一种方法对象

## Inputs

- skill 名称
- skill 边界
- 预期触发场景

## Steps

1. 先证明这真的是一个独立能力边界。
2. 设计目录名、总入口和最少必要文件。
3. 如需加速建空骨架，可运行 [../scripts/create_skill_scaffold.py](../scripts/create_skill_scaffold.py)。
4. 先写 `SKILL.md`，把对象、触发条件、最短路径和相邻 skill 说清。
5. 再写至少一份真实 reference 和至少一条真实 workflow。
6. 若对象需要额外解释，再补 `docs/`；若对象需要确定性辅助，再补 `scripts/`。

## Outputs

- 一个最小可用的新 skill

## Verification

- 读者只看 `SKILL.md` 是否知道如何进入本 skill
- 新 skill 是否拥有至少一条真实 workflow
- 新 skill 是否拥有至少一份真实 reference
- 新 skill 是否只建立了当前对象真正需要的附属面
- 脚手架是否仍停留在占位层

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../scripts/create_skill_scaffold.py](../scripts/create_skill_scaffold.py)
