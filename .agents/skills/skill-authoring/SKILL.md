---
name: skill-authoring
description: 立即启用：当任务已经进入 skill 本身的建设、重构、目录编排、入口组织、链接回路或脚手架设计。
---

# Skill Authoring

一个 skill 如果只是一组文件，它很快就会退化成资料夹。有人补一篇说明，有人加一条 workflow，有人再添几份 reference，看上去内容越来越多，真正的入口却越来越弱。读者第一次进入 skill 时看不出来先读什么、什么时候跳走、哪些文件是静态真值、哪些文件只是解释，最后 skill 变成一个摆资料的目录。

这里把 skill 当成一种需要被设计、编写和维护的工具。工具要能被触发、能被阅读、能被修订、能被继续扩展，所以它必须拥有清楚的总入口、稳定的内部结构、真实的文件回链和明确的相邻 skill 关系。跨 skill 导航也放在这里处理，它本来就是 skill 自身的结构问题。

## 最短路径

1. 先读 [workflows/create-skill.md](workflows/create-skill.md)
2. 需要重构现有 skill 时，读 [workflows/revise-skill.md](workflows/revise-skill.md)
3. 需要核对根入口、skill 结构和关键回链时，读 [workflows/inspect-entry-surface.md](workflows/inspect-entry-surface.md)
4. 再查 [references/STRUCTURE.md](references/STRUCTURE.md)
5. 需要补“最小结构”和“最小可用状态”的区别时，读 [docs/skill-system.md](docs/skill-system.md)

## 文件导航

- [references/REFERENCE.md](references/REFERENCE.md)
- [references/STRUCTURE.md](references/STRUCTURE.md)
- [workflows/create-skill.md](workflows/create-skill.md)
- [workflows/revise-skill.md](workflows/revise-skill.md)
- [workflows/inspect-entry-surface.md](workflows/inspect-entry-surface.md)
- [docs/skill-system.md](docs/skill-system.md)
- [scripts/create_skill_scaffold.py](scripts/create_skill_scaffold.py)

## 使用约束

- `SKILL.md` 必须承担总入口
- 脚手架脚本只生成空骨架
- 新文件只有在能回到 skill 主结构时才值得建立
