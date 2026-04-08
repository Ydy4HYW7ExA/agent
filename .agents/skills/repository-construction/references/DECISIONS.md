# Repository Construction Decisions

仓库建设能不能落地，取决于几个关键条件有没有被写实。条件没有被写实，后续结构就会停留在“看上去像对”的状态。

## 构成性上游依赖

`compositional upstream dependency` 指两条条件同时成立的上游依赖：

1. 当前包对外提供的能力部分由这个上游能力构成。
2. 上游带来的协议、数据形状、错误语义或接口语言，需要被翻译成当前包统一语言。

下表给出默认归类。它不代替最后判断，但它提供第一轮判断：

| 对象 | 默认归类 |
| --- | --- |
| 另一个内部业务包 | 归为构成性上游依赖 |
| RPC/HTTP client | 返回结果进入业务判断时，归为构成性上游依赖 |
| 第三方 SDK | SDK 语言需要被翻译时，归为构成性上游依赖 |
| 数据库驱动 | 数据库结果直接进入业务判断时，归为构成性上游依赖 |
| cache client | 缓存值直接进入业务判断时，归为构成性上游依赖 |
| message queue client | 消息体进入业务判断时，归为构成性上游依赖 |
| logger / metrics / tracer | 一般不归为构成性上游依赖 |
| 时钟 / UUID / env reader | 一般不归为构成性上游依赖 |

## 独立验证责任面

`validation surface` 不等于“包里有测试”。验证对象、验证逻辑或验证出口已经形成独立责任面时，建立 `tests` 语义区。信号如下：

| 信号 | 说明 |
| --- | --- |
| 需要可复用的测试夹具或测试数据工件 | 验证已形成自己的对象 |
| 需要契约测试或对外验证出口 | 验证已形成自己的边界 |
| 验证逻辑本身已经很厚 | 验证已经形成自己的责任面 |

## 实现变体

`implementation variant` 只在下面三条同时成立时才值得出现：

1. 它仍然承接同一个 `package language`。
2. 它仍然暴露同一组出入口职责。
3. 它不会把旧包边界偷换成新包边界。

若当前只是想试一个新语言方向、但还没有稳定公开行为，不要直接把它升成 `implementation variant`。先把它写进草稿工件，确认它要承接的是同一个包，而不是一个新包。

当一个包里出现多个 `implementation variant` 时，至少再补两项：

1. 一份 `equivalence contract`
2. 一份 `conformance suite`

若没有这两项，就不把“并列多语言实现”提升成稳定结构，而只把它视为过渡状态。

## 拆分信号

`split signal` 的主判断是：任一 `business/exit` 文件，是否直接依赖了多于一个 `business` 非出口文件。

| 情况 | 判断 |
| --- | --- |
| 某个 `business/exit` 直接依赖多个 `business` 非出口文件 | 拆分信号 |
| 某个 `business/exit` 只直接依赖一个 `business` 非出口文件 | 允许 |
| 某个 `business/exit` 只依赖其他 `business/exit` | 先不判拆分，继续人工核对真实依赖链 |

这条规则的落手顺序如下：

1. 先列出每个 `business/exit` 文件的一跳直接依赖。
2. 只统计其中落在 `business` 非出口区域的文件数。
3. 若某个出口对应数量大于 1，标记 `split signal`。
4. 若没有任何出口超过 1，先不下拆分结论。

这种草稿工件的最小对象如下：

```json
{
  "business_exit_file": "",
  "direct_business_internal_dependencies": [],
  "current_decision": "unknown"
}
```

## 包销毁信号

包的销毁信号只有一个：`src/business/exit/` 下没有任何文件。

这条规则的意义不是“目录空了立刻删”，而是说明当前包已经失去业务出口，不再承接活需求。真正删除目录前，仍要先走迁移或退役流程。

最小判断对象如下：

```json
{
  "business_exit_files": [],
  "current_decision": "retire_when_empty"
}
```

## Wrappers 的双出入口集合

一旦 `wrappers` 出现，`entry/` 与 `exit/` 一起出现。`entry` 负责接入上游依赖，`exit` 负责暴露翻译结果。这里不建立额外 `root`；封装区内部实现直接落在语义区剩余位置。

## 文件名

固定的是目录位置，不是文件命名模式。`entry file` 与 `exit file` 的数量和文件名都自由，只要它们落在正确目录，并且关系规则能被核对。

这份文件里的判断都按同一条总规则使用：

```json
{
  "decision_rule": {
    "when_clear": "write it into structure object",
    "when_unclear": "write it into draft artifact first",
    "never_do": "promote uncertainty into stable structure"
  }
}
```
