---
name: collaboration-dialogue
description: 立即启用：当用户表达仍混杂对象、动作、情绪、临时命名和跳跃视角，导致任务还不能直接落到其他 skill。
---

# Collaboration Dialogue

用户在对话里会同时做很多事：指对象、试探方案、表达不满、随手起名、来回切换视角。交流现场容得下这种混杂，因为目标是逼近问题；长期结构容不下这种混杂，因为长期结构要求对象、边界和动作都能被稳定复用。现场语言一旦原样搬进术语、工作流或仓库文档，后面的所有文件都会继承同样的混乱。

这里要处理的对象，是当前任务窗口内尚未正式化的对话材料。窗口可以跨越多轮，不以单轮消息为界；只要某些说法还没有被清洗并固化到任务、术语或长期文档里，它们仍然属于原始材料。后续工作真正要用的，是从这些材料里收出来的稳定对象、边界、动作、下一跳和预期工件。

## 最短路径

1. 先读 [workflows/clean-request.md](workflows/clean-request.md)
2. 再查 [references/TERMINOLOGY.md](references/TERMINOLOGY.md)
3. 需要把清洗结果收成执行入口时，读 [workflows/shape-task-path.md](workflows/shape-task-path.md)
4. 需要补“任务窗口”和草稿工件落点时，读 [docs/conversation-window.md](docs/conversation-window.md)

## 文件导航

- [references/REFERENCE.md](references/REFERENCE.md)
- [references/TERMINOLOGY.md](references/TERMINOLOGY.md)
- [workflows/clean-request.md](workflows/clean-request.md)
- [workflows/shape-task-path.md](workflows/shape-task-path.md)
- [docs/conversation-window.md](docs/conversation-window.md)

## 使用约束

- 用户原话不直接进入规则、术语、定义或长期说明
- 清洗后的表达必须能指出对象、动作、边界、下一跳和预期工件
- 任务一旦成形，主入口立刻交给后续 skill

## 下一跳

清洗后的表达若先出在命名漂移，继续进入 [terminology-governance](../terminology-governance/SKILL.md)。若先出在文档落点和正文写法，继续进入 [documentation-authoring](../documentation-authoring/SKILL.md)。若对象已经是 skill 本身的建设或重构，继续进入 [skill-authoring](../skill-authoring/SKILL.md)。若对象已经是仓库、包和结构工件，继续进入 [repository-construction](../repository-construction/SKILL.md)。
