# agent

这个仓库用于建设一套可复用的 agent 工作体系。它不承接具体业务产品实现，也不充当某个业务仓库的项目文档目录。这里承接的是会被反复进入、反复修订、还能继续反过来建设自己的方法对象。

顶层路径刻意保持收紧。根 [AGENTS.md](../AGENTS.md) 只写通用协作规则，不写仓库用途细节；这个 README 负责说明仓库语境和顶层结构；`.agents/skills/` 承接具体方法对象；根 `scripts/` 只保留仓库级维护工具；`temp/` 只承接当前轮的草稿材料，不进入长期真值。

当前仓库的顶层结构如下：

```text
agent/
├── AGENTS.md
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── event-system-thinking-notes.md
│   └── roadmap.md
├── .agents/
│   └── skills/
├── scripts/
│   └── clean_repository_cache.py
├── temp/
└── .gitignore
```

顶层路径职责如下：

| 路径 | 承接对象 | 不承接什么 |
| --- | --- | --- |
| `AGENTS.md` | 通用协作规则 | 仓库用途细节 |
| `docs/` | 仓库级事实与结构说明 | skill 内部静态真值 |
| `.agents/skills/` | 方法对象 | 仓库事实 |
| `scripts/` | 仓库维护工具 | 方法脚手架 |
| `temp/` | 当前草稿工件 | 长期真值 |

当前仓库启用五个核心 skills。它们不是五个话题目录，而是五种稳定方法入口。

| skill | 处理对象 |
| --- | --- |
| [collaboration-dialogue](../.agents/skills/collaboration-dialogue/SKILL.md) | 混杂表达的清洗 |
| [terminology-governance](../.agents/skills/terminology-governance/SKILL.md) | 正式术语与迁移 |
| [documentation-authoring](../.agents/skills/documentation-authoring/SKILL.md) | 文档落点与写法 |
| [skill-authoring](../.agents/skills/skill-authoring/SKILL.md) | skill 自举与重构 |
| [repository-construction](../.agents/skills/repository-construction/SKILL.md) | 仓库与包结构建设 |

根 `scripts/` 目录当前只有一个脚本：[clean_repository_cache.py](../scripts/clean_repository_cache.py)。原因很直接：缓存清理属于仓库级卫生；脚手架和方法辅助脚本都下沉到对应的 skill。根目录不承接方法对象自己的脚本边界。入口完整性、导航回链和结构收束通过 [skill-authoring](../.agents/skills/skill-authoring/SKILL.md) 的人工核对 workflow 维护。

阅读顺序保持固定。先读 [AGENTS.md](../AGENTS.md)，再读这个 README。对象已经明确时，直接进入对应 skill 的 `SKILL.md`；需要补“这套体系的对象链和 skill 关系”时，读 [architecture.md](architecture.md)；需要补当前建设状态时，读 [roadmap.md](roadmap.md)。

当前项目自身的系统思考笔记已整理成 [event-system-thinking-notes.md](event-system-thinking-notes.md)。这份文档承接项目级讨论结果，完整保留当前系统方向、关键对象、主要判断、可参考项和未定项，避免后续继续依赖聊天上下文。

当前仓库已经站住主入口、三个基础 skills、skill 自举方法，以及仓库建设里的结构、运行时建模和包体系演化对象。后续扩展只在新的稳定对象真正出现时才进入主结构；根入口不再预设新的厚文目录。
