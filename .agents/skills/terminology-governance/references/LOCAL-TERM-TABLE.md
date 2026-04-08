# Local Term Table

局部术语表是具体文件，不是抽象概念。默认情况下，某个 skill 的局部术语表写在：

```text
<skill-root>/references/TERMINOLOGY.md
```

某个 skill 还没有形成足够多的局部对象时，可以暂不建立这张表；一旦开始频繁谈论局部对象、局部边界和局部判断条件，就应显式建立。

局部术语表的最小记录格式如下：

| 术语 | 状态 | 定义 | 边界 | 备注 |
| --- | --- | --- | --- | --- |
| `example term` | `formal` | 它指什么 | 它不指什么 | 关联文件 |
| `old term` | `deprecated` | 历史叫法 | 不再作为主词 | `replaced_by: new term` |
| `helper name` | `alias` | 迁移期对照词 | 不占入口 | `alias_of: formal term` |

相同内容也可以写成结构对象：

```json
{
  "term": "",
  "status": "formal | alias | deprecated",
  "definition": "",
  "boundary": "",
  "link": "",
  "relation": "replaced_by | alias_of | none"
}
```

关键入口的最小清单也要固定。术语替换时，至少检查：

```json
{
  "entry_surfaces": [
    "root AGENTS.md when affected",
    "root docs/README.md when affected",
    "affected SKILL.md",
    "affected local term tables",
    "affected workflows"
  ]
}
```
