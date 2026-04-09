# Architecture

用户问题不会直接变成代码、文档或脚本。更稳的做法，是先把问题收成稳定对象，再把这些对象送进对应的方法入口。没有这条中间链，仓库里的文件就会不断把聊天残留、命名漂移和临时判断带进长期结构。

当前方法体系的总工作链如下：

```text
raw material
-> clean expression
-> task path
-> target skill
```

这条链里的前三个节点是工作对象，最后一个节点是当前任务路径首先进入的方法入口。`raw material` 承接当前任务窗口里的原始材料，不承接长期真值。`clean expression` 把原始材料收成稳定对象、动作和边界，不承接正式执行路径。`task path` 把清洗结果收成可执行入口，执行动作从这里开始脱离聊天原话。`target skill` 则按当前问题首先落在哪个对象面来决定；它可能是 [terminology-governance](../.agents/skills/terminology-governance/SKILL.md)、[documentation-authoring](../.agents/skills/documentation-authoring/SKILL.md)、[skill-authoring](../.agents/skills/skill-authoring/SKILL.md) 或 [repository-construction](../.agents/skills/repository-construction/SKILL.md)。

术语治理和文档落点属于常见下一跳，但不是默认必经层。更准确的理解是：任务路径若先出在命名治理，就先进入 `terminology-governance`；若先出在文档对象，就先进入 `documentation-authoring`；若对象已经是 skill 本身或仓库结构本身，就直接进入对应的建设 skill。它们是 `target skill` 的候选入口，不是总链上每次都会经过的固定节点。

五个核心 skills 共同覆盖这条链，但各自只承接一段明确边界：

| skill | 主对象 | 下一跳 |
| --- | --- | --- |
| [collaboration-dialogue](../.agents/skills/collaboration-dialogue/SKILL.md) | 对话材料 | `terminology-governance` / `documentation-authoring` / `skill-authoring` / `repository-construction` |
| [terminology-governance](../.agents/skills/terminology-governance/SKILL.md) | 正式命名 | `documentation-authoring` / `skill-authoring` / `repository-construction` |
| [documentation-authoring](../.agents/skills/documentation-authoring/SKILL.md) | 文档对象 | `skill-authoring` / `repository-construction` |
| [skill-authoring](../.agents/skills/skill-authoring/SKILL.md) | skill 本身 | 继续扩展 skill 体系 |
| [repository-construction](../.agents/skills/repository-construction/SKILL.md) | 仓库与包结构 | 继续落到代码、注释、文档和脚本边界 |

工具依赖图说明“一个 skill 在处理自己的对象时，需要借用哪些方法”；下一跳图说明“工作流在进入某个 skill 后，会往哪类问题流转”。这两种关系不能混成一张图。

工具依赖图如下：

```json
{
  "collaboration-dialogue": [],
  "terminology-governance": [],
  "documentation-authoring": [
    "collaboration-dialogue",
    "terminology-governance"
  ],
  "skill-authoring": [
    "documentation-authoring",
    "terminology-governance"
  ],
  "repository-construction": [
    "collaboration-dialogue",
    "terminology-governance",
    "documentation-authoring"
  ]
}
```

下一跳图如下：

```json
{
  "collaboration-dialogue": [
    "terminology-governance",
    "documentation-authoring",
    "skill-authoring",
    "repository-construction"
  ],
  "terminology-governance": [
    "documentation-authoring",
    "skill-authoring",
    "repository-construction"
  ],
  "documentation-authoring": [
    "skill-authoring",
    "repository-construction"
  ]
}
```

根目录与 skill 的关系必须守住。根目录只承接通用协作规则、仓库级事实和阅读入口；具体方法对象下沉到 [`.agents/skills/`](../.agents/skills)。如果根目录开始重复 skill 的术语定义、工作流步骤或局部结构判断，仓库很快就会长出两套并列入口。

`temp/` 也是这套结构中的显式一层。它承接当前轮仍未正式化的草稿工件，作用是防止临时判断既不进正式文档，又不断在聊天中漂移。`temp/` 是工作对象区，不是真值区；内容一旦进入正式文档或正式方法对象，就应退出 `temp/`。
