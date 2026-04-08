# Collaboration Dialogue Terminology

`raw material` 指当前任务窗口内尚未正式化的对话材料。它可以来自一轮，也可以来自多轮；判断标准看它是否已经被清洗并固化。

`clean expression` 指已经被收成稳定对象、动作、边界、下一跳和预期工件的表达。它仍然可以写成自然段；在工作层面，它必须能还原为固定字段。

`dialogue residue` 指对执行没有直接帮助、却容易污染正式结构的聊天残留，例如情绪句、比喻句、临时口头简称和跳跃视角。

`task path` 指已经可以直接进入执行的任务表达。它的最小形状如下：

```json
{
  "object": "",
  "action": "",
  "boundary": "",
  "next_step": "",
  "expected_artifact": ""
}
```

`clean expression` 和 `task path` 使用同一组字段。二者的区别只在于：`clean expression` 还停留在清洗阶段，`task path` 已经进入执行。
