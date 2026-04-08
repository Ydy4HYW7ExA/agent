# Skill Authoring Structure

skill 的最小目录结构和最小可用状态是两道不同门槛，必须分开。

最小目录结构只要求：

```text
<skill-root>/
├── SKILL.md
├── references/
└── workflows/
```

如果对象需要额外解释或确定性辅助，再显式增加：

```text
<skill-root>/
├── docs/        # optional
└── scripts/     # optional
```

`docs/` 和 `scripts/` 只在对象需要时出现；它们不属于每个 skill 的最小必有目录。

最小可用 skill 则要求下面四件事同时成立：

```json
{
  "entry": "real SKILL.md",
  "truth": "at least one real reference file",
  "execution": "at least one real workflow",
  "navigation": "entry links to the other three"
}
```

脚手架脚本的边界必须写死。它做三件事：建立目录、建立极薄占位文件、生成标题骨架。跑完脚手架以后，还要补齐一份真实的 `SKILL.md`、一份真实的 reference、以及一条真实 workflow。这样，skill 才真正拥有可用入口。

当前脚手架默认会补三件占位工件：

```json
{
  "scaffold_outputs": [
    "SKILL.md",
    "references/REFERENCE.md",
    "workflows/WORKFLOW.md"
  ]
}
```

这三件工件只保证入口没有塌，不代表 skill 已可用。`workflows/WORKFLOW.md` 只是把任务路径的承接位置先占住；真实 workflow 仍要随后补写。
