# Terminology Governance Terminology

`formal term` 指系统中的唯一主表述。它对应一个稳定对象，并且给出定义、边界和落点。

`local term` 指只在单个 skill 或单个对象边界内成立的术语。局部术语可以很重要；重要不自动推出升格。

`alias` 指为了迁移、检索或对照而保留的别名。别名帮助读者对照；它不占据主入口。

`deprecated term` 指已经退出主表述位置的历史叫法。它明确指向当前正式术语。

`canonical terms` 指共享术语总表。一个词进入总表，有两种合法路径：

```json
{
  "promote_when": [
    "the term is reused across at least two skills",
    "the term is a system-level entry object"
  ]
}
```

共享总表不只记录“为什么进入”，还要承担共享主定义。根入口和局部 skill 若要使用这些词，只做最小释义并回链到这里，不再各自长出一套入口定义。

当前共享总表如下：

| 术语 | 定义 | 边界 | 主落点 | 进入总表的理由 |
| --- | --- | --- | --- | --- |
| `skill` | 一组可被触发、可被阅读、可被修订的稳定方法对象 | 不等于任意资料目录，也不等于临时话题标签 | `.agents/skills/<skill-name>/SKILL.md` | 五个 skills 都直接依赖它 |
| `workflow` | 把任务路径写成可执行步骤的文件对象 | 不等于静态真值，也不等于长篇解释 | `<skill-root>/workflows/*.md` | 所有 skills 都用它承接任务路径 |
| `reference` | 收口静态真值、定义和固定判断条件的文件对象 | 不等于步骤说明，也不等于临时草稿 | `<skill-root>/references/*.md` | 所有 skills 都用它承接静态真值 |
| `clean expression` | 已被收成稳定对象、动作、边界、下一跳和预期工件的表达 | 不等于原始对话材料，也还没有进入正式执行路径 | `.agents/skills/collaboration-dialogue/references/TERMINOLOGY.md` | 从对话清洗进入后续工作时共享使用 |
| `formal term` | 系统中的唯一主表述，它对应一个稳定对象，并给出定义、边界和落点 | 不等于 alias，也不等于 deprecated term | `.agents/skills/terminology-governance/references/TERMINOLOGY.md` | 所有术语治理动作都围绕它展开 |
| `repository root` | 仓库顶层入口与仓库级事实所在的位置 | 不等于所有实现面，也不等于任意顶层目录集合 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为系统级入口对象 |
| `package root` | 围绕单一需求边界建立的包级承接对象 | 不只是目录容器，也不等于任意实现子树 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为系统级入口对象 |
| `implementation variant` | 同一个包边界下、以某种语言给出的等价实现变体 | 不等于新包，也不等于任意第二套实现草稿 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为跨对象复用的系统级入口对象 |
| `runtime triad` | 由 `protocol`、`client kernel` 与 `server kernel` 组成的关系抽象 | 不等于任一实例，也不等于任一实例包 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为运行时建模的系统级入口对象 |
| `instance package` | 承接某一侧可运行实例的包对象 | 不等于关系抽象，也不等于任意实现子树 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为运行时建模的系统级入口对象 |
| `minimal business domain package group` | 由一份 `runtime triad` 与两侧 `instance package` 共同构成的最小业务域包群 | 不等于单个包，也不等于单条过程边 | `.agents/skills/repository-construction/references/TERMINOLOGY.md` | 它已经成为运行时建模的系统级入口对象 |
