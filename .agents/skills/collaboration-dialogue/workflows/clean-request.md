# Clean Request

## Purpose

把一段仍然混杂的用户表达收成干净输入。

## Use When

- 当前还不能直接指出对象边界
- 原话里混着诉求、评价、比喻和方案
- 多轮对话里已经累积出一堆未整理材料

## Inputs

- 当前任务窗口内的对话材料
- 当前上下文

## Steps

1. 先提对象：这堆材料真正指向的对象是什么，哪些内容只是陪衬。
2. 再提动作：用户现在要推进、替换、否定、比较还是停止什么。
3. 补边界：哪些内容属于当前任务，哪些只是背景、例子或情绪。
4. 明确下一跳和预期工件。
5. 把结果写成 `clean expression` 对象；必要时再把它改写成自然段。

## Outputs

- 一份 `clean expression`

## Verification

- 输出是否包含对象、动作、边界、下一跳和预期工件
- 新表达是否已经摆脱原话顺序和噪声
- 读者是否能仅凭清洗结果判断后续应进入哪个 skill

## Related

- [../references/TERMINOLOGY.md](../references/TERMINOLOGY.md)
- [../docs/conversation-window.md](../docs/conversation-window.md)
