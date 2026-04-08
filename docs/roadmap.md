# Roadmap

当前仓库处于主结构收束期。目标是让根入口、核心 skills 和仓库建设方法保持同一套稳定边界。

当前阶段对象如下：

```json
{
  "stage": "stabilizing",
  "active_tracks": [
    "root entry surface",
    "three foundation skills",
    "skill self-authoring",
    "repository construction",
    "runtime-model workflow",
    "package-system evolution"
  ],
  "deferred_tracks": []
}
```

当前已决定建设的对象按批次展开如下：

| 批次 | 当前状态 | 下一步 |
| --- | --- | --- |
| 根入口面 | `active` | 继续保持根规则、根说明和根脚本边界稳定 |
| 基础 methods | `active` | 继续维护 collaboration、terminology、documentation 三个基础 skill |
| skill 自举 | `active` | 继续维护 `skill-authoring` |
| 仓库建设 | `active` | 继续维护结构、运行时建模和包体系演化 |

当前活入口依赖的主文件如下：

| 入口层 | 主文件 |
| --- | --- |
| 根规则 | [AGENTS.md](../AGENTS.md) |
| 仓库说明 | [README.md](README.md) |
| 对象关系 | [architecture.md](architecture.md) |
| 表达清洗 | [collaboration-dialogue](../.agents/skills/collaboration-dialogue/SKILL.md) |
| 术语治理 | [terminology-governance](../.agents/skills/terminology-governance/SKILL.md) |
| 文档写作 | [documentation-authoring](../.agents/skills/documentation-authoring/SKILL.md) |
| skill 自举 | [skill-authoring](../.agents/skills/skill-authoring/SKILL.md) |
| 仓库建设 | [repository-construction](../.agents/skills/repository-construction/SKILL.md) |

当前明确不进入根结构的对象如下：

| 对象 | 当前决定 | 原因 |
| --- | --- | --- |
| 根完整性检查脚本 | 不进入根 | 根脚本边界收紧到仓库卫生；入口完整性由人工 workflow 承接 |
| 第二个仓库级脚手架目录 | 不建立 | 方法脚本按 skill 下沉 |
| 额外根说明文集 | 不预设 | 根入口只承接仓库级事实与阅读路径 |

当前最容易失真的风险也要显式写出。第一，术语会继续升格到失去收紧。第二，根目录会吸收本该下沉到 skill 的细节。第三，方法脚本会上浮到根 `scripts/`，让仓库脚本边界变宽。第四，`repository-construction` 会在没有新稳定对象时继续长厚。

后续变化条件也必须写死。只有当新的稳定对象已经出现，而且现有 skill 不能自然承接它时，才继续扩结构。当前体系已经拥有可工作的厚骨架；下一步重点不在增文件数量，而在继续保持边界稳定。
