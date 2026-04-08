# Rules

这里定义通用协作规则，不解释当前仓库承接什么对象。`skill`、`workflow`、`reference` 等共享术语的主定义落在 [terminology-governance/references/TERMINOLOGY.md](.agents/skills/terminology-governance/references/TERMINOLOGY.md)。当前仓库自己的用途、顶层路径和阅读顺序写在 [docs/README.md](docs/README.md)。需要进入稳定方法时，读 [`.agents/skills/`](.agents/skills) 下的具体 skill。

与用户对话时，先清洗用户语言，再进入正式表达。清洗不是抽象要求，而是把原话中的对象、动作、边界、条件、约束和预期工件拆开。聊天现场的比喻、情绪、口头简称和跳跃视角可以帮助理解；这些内容不直接进入术语、规则、工作流或长期说明。

工作入口直接挂到 skill 和 workflow。workflow 在这里承接任务路径：遇到哪种情形，应先做什么判断，再做什么动作，最后如何核对结果。已经能进入 skill 的问题，直接进入对应方法入口。额外流程不在根目录建立。

信息落点要守住。通用方法、稳定规则、共享术语、工作流和必要解释进入 [`.agents/skills/`](.agents/skills)；仓库级事实与说明进入 [docs/README.md](docs/README.md) 或 [docs/architecture.md](docs/architecture.md)；代码局部的边界、意图和异常进入注释；临时分析材料若需要持久化，则进入 `temp/`。相同知识只保留一个主落点。

当前仓库的落点边界如下：

| 信息类型 | 主落点 | 不应落在 |
| --- | --- | --- |
| 通用方法 | `.agents/skills/` | 根 `docs/` |
| 仓库级事实 | `docs/README.md` | skill reference |
| 代码局部边界 | 注释 | README |
| 临时分析材料 | `temp/` | 正式文档 |

表达方式保持稳定。中文正文，英文文件名和目录名。自然段先把对象和判断说完整，再用表格、目录树、JSON 片段或关系块展开。结构化元素负责压实边界，不负责替代正文。关系统一写成 `A -> B` 或 `A -X-> B`。

当前问题进入仓库的方法链如下：

```text
raw material
-> clean expression
-> task path
-> target skill
```

如果当前问题先出在表达混乱、对象未明、任务未成形，进入 [collaboration-dialogue](.agents/skills/collaboration-dialogue/SKILL.md)。如果当前问题先出在命名漂移、别名混用、术语未稳，进入 [terminology-governance](.agents/skills/terminology-governance/SKILL.md)。如果当前问题先出在文档怎么写、信息怎么落点、结构化元素怎么使用，进入 [documentation-authoring](.agents/skills/documentation-authoring/SKILL.md)。如果当前任务是在建设或重构 skill 本身，进入 [skill-authoring](.agents/skills/skill-authoring/SKILL.md)。如果当前任务已经进入仓库建设对象本身，进入 [repository-construction](.agents/skills/repository-construction/SKILL.md)。

禁止为了交付速度而牺牲架构。根目录、`docs/`、`.agents/skills/` 和根 `scripts/` 共同构成当前仓库唯一有效的主结构。入口完整性通过 skill 内部 workflow 做人工核对，不由根脚本承担。
