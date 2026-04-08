# Inspect Entry Surface

## Purpose

人工核对当前活入口是否仍然收束，防止根入口、skill 入口和共享术语表长散。

## Use When

- 第一轮建设之后需要做一次结构收束
- 修改了根入口、共享术语、skill 导航或关键 workflow 之后
- 怀疑仓库正在长出第二套活入口

## Inputs

- 根入口文件
- 当前 skills 目录
- 当前共享术语总表

## Steps

1. 先看根入口：确认 `AGENTS.md` 只承接通用协作规则，`docs/README.md` 只承接仓库事实，根 `scripts/` 只承接仓库维护工具。
2. 再看每个 `SKILL.md`：确认它都回链 `references/REFERENCE.md`、自己的 workflow、必要 docs 和必要 scripts。
3. 回看共享术语总表：确认共享词保持收紧，没有把局部词提前升格。
4. 回看 skill 的局部 terminology：确认新的局部词没有绕过共享总表与局部表的边界。
5. 若发现某条知识同时在根入口和 skill 内部长出两份主说明，立刻决定唯一主落点，并把另一处降回最小释义或回链。
6. 若发现某个 workflow 已经承担静态真值，或某个 reference 已经开始承接步骤，立刻把文件职责重新分开。

可以用下面这个最小检查对象承接每轮核对：

```json
{
  "root_entry": {
    "agents_md_only_carries_rules": true,
    "readme_only_carries_repository_facts": true,
    "root_scripts_only_carry_repository_maintenance": true
  },
  "skill_entry": {
    "every_skill_md_links_reference_index": true,
    "every_skill_md_links_workflows": true,
    "every_skill_md_links_needed_docs_and_scripts": true
  },
  "terminology": {
    "shared_term_table_is_still_tight": true,
    "local_terms_do_not_bypass_local_tables": true
  }
}
```

## Outputs

- 一轮完成的入口面人工核对

## Verification

- 根入口是否只有一套
- 每个 `SKILL.md` 是否承担总入口
- 共享术语总表是否保持收紧
- 文件职责是否分开
- 检查对象里的三组字段是否都还能给出 `true`

## Related

- [../references/STRUCTURE.md](../references/STRUCTURE.md)
- [../../terminology-governance/references/TERMINOLOGY.md](../../terminology-governance/references/TERMINOLOGY.md)
- [../../documentation-authoring/references/WRITING.md](../../documentation-authoring/references/WRITING.md)
