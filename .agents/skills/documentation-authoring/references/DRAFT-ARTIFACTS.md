# Draft Artifacts

草稿工件用来承接仍在形成中的分析材料。它们是工作对象；它们不进入长期真值。只有在需要跨轮保存、跨人协作或明确引用时，草稿工件才值得被持久化；否则它可以停留在对话上下文中。

若需要持久化，默认落点是目标仓库自己的 `temp/`。按作用域可以分成三类：

```json
{
  "draft_locations": {
    "task_scoped": "temp/tasks/",
    "architecture_scoped": "temp/architecture/",
    "skill_scoped": "temp/skills/"
  }
}
```

草稿工件的生命周期只有三种状态：

| 状态 | 含义 | 下一步 |
| --- | --- | --- |
| `active` | 仍在形成中 | 继续修改 |
| `promoted` | 已进入正式文档或正式对象 | 删除或回链后退出 |
| `abandoned` | 已失去作用 | 删除 |

草稿不长期停留在灰区。内容进入正式文档后，它移出任务窗口；内容失效后，它删除。
