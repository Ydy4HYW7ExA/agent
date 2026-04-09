# Repository Construction Relations

包内关系必须下沉到文件级才算成立。目录名只能提示语义，不能替代依赖判断。每个包都按独立 `bounded context` 理解；这个工作范围维护自己的统一语言，包外对象进入包内时不能直接携带外来语言横穿内部实现。

当前采用三个语义区：`wrappers`、`business`、`tests`。`business` 是必有区，它承接当前包的问题边界和统一语言。`wrappers` 在存在构成性上游依赖时出现。`tests` 在独立验证责任面成立时出现。

当前固定出入口只有两类：`entry file` 与 `exit file`。固定的不只是目录位置，还有文件命名规则：固定点文件统一采用 `<suffix>.<suffix>` 形式。`wrappers` 拥有 `entry/` 与 `exit/`；`business` 与 `tests` 只拥有 `exit/`。其余源码文件都按 `internal source file` 理解。

关系规则按“禁止什么”优先表达。没有被这里禁止的同区内部依赖，不额外制造主次。

| 位置 | 允许依赖 | 禁止依赖 |
| --- | --- | --- |
| `src/wrappers/entry/**` | `src/wrappers/**` 之外的文件、标准库、第三方库、`config/wrappers/**` | 任意 `src/wrappers/**` |
| `src/wrappers/**` 中除 `entry/` 与 `exit/` 外的文件 | 同区内部实现、`src/wrappers/entry/**`、`config/wrappers/**` | `src/wrappers/exit/**` |
| `src/wrappers/exit/**` | 同区内部实现、同区其他 `exit` 文件、`config/wrappers/**` | `src/wrappers/entry/**`、任意 `src/wrappers/**` 之外的源码文件 |
| `src/business/**` 中除 `exit/` 外的文件 | 同区内部实现、`src/wrappers/exit/**`、`config/business/**` | 任意包外源码文件 |
| `src/business/exit/**` | 同区内部实现、同区其他 `exit` 文件、`config/business/**` | 任意 `src/business/**` 之外的源码文件 |
| `src/tests/**` 中除 `exit/` 外的文件 | 同区内部实现、`src/wrappers/exit/**`、`src/business/exit/**`、`config/tests/**` | 任意包外源码文件 |
| `src/tests/exit/**` | 同区内部实现、同区其他 `exit` 文件、`config/tests/**` | 任意 `src/tests/**` 之外的源码文件 |

几条关键禁止关系如下：

```json
{
  "forbidden": [
    "wrappers entry -> any file under wrappers",
    "wrappers internal -> wrappers exit",
    "wrappers exit -> wrappers entry",
    "wrappers exit -> source files outside wrappers",
    "business exit -> source files outside business",
    "tests exit -> source files outside tests"
  ]
}
```

这里还有三条补充理解：

1. `business` 非出口文件可以依赖 `wrappers/exit`。
2. `tests` 非出口文件可以依赖 `wrappers/exit` 与 `business/exit`。
3. 拆分信号只看某个 `business/exit` 对 `business` 非出口文件的一跳直接依赖数，不看传递依赖，也不看它对同区其他出口文件的依赖。

关系规则对多变体包同样成立。`implementation variant` 可以并列存在，但并列不改写固定点规则。读者应当先从目录判断固定点语义，再从 `<suffix>.<suffix>` 判断当前查看的是哪一个实现变体的固定点文件。

把这组规则压成两个最小例子，会更容易落手。

```text
legal:
src/business/internal/pool.ts -> src/wrappers/exit/ts.ts
src/business/exit/ts.ts -> src/business/internal/pool.ts
```

上面这组关系合法，因为 `business` 非出口文件可以依赖 `wrappers/exit`，而 `business/exit` 只继续依赖本区内部实现。

```text
illegal:
src/wrappers/entry/ts.ts -> src/wrappers/internal/session.ts
src/wrappers/exit/ts.ts -> src/business/internal/pool.ts
```

上面这组关系不合法，因为 `wrappers/entry` 不碰 `wrappers` 区内源码，而 `wrappers/exit` 也不碰 `wrappers` 区外源码。只要出现这类依赖，关系核对结果就不应再写成“通过”。
