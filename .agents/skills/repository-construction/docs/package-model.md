# Package Model

`package root` 指围绕单一需求边界建立的包级承接对象。`package language` 指当前包内部业务判断所使用的统一语言。`bounded context` 指围绕同一问题边界和统一语言成立的工作范围。后面会反复用到这三个词，所以先把它们站住。

包出现的条件是：某个对象已经形成单一需求边界，并且需要拥有自己的长期承接面。所谓承接面，包括固定出入口、内部实现、配置位置、统一语言和生命周期判断。对象还没稳，就不建包；对象已经稳定时，包才有出现理由。

每个包都按独立 `bounded context` 理解。这里的“独立”不表示它不依赖任何别的对象；它表示一旦进入这个包，后续业务判断都围绕这个包自己的问题边界和统一语言展开。包外语言可以存在；包内语言不因此失守。

`core structure` 指包为了站住自己的问题边界、统一语言和固定出入口而必须拥有的结构。`optional surfaces` 指包按自己需要增加的附属面，例如 `docs/`、`scripts/`、`fixtures/`、`temp/`。包和仓库一样，都是自由对象；规则真正约束的是核心结构，不约束自由附属面的上限。

当前固定语义区是 `wrappers`、`business`、`tests`。`wrappers` 只在存在构成性上游依赖时出现；`business` 是必有区；`tests` 只在独立验证责任面成立时出现。

当前固定出入口只有两类：`entry file` 与 `exit file`。`wrappers` 拥有 `entry/` 与 `exit/`；`business` 与 `tests` 只拥有 `exit/`。语义区剩余源码文件统一按自由内部实现处理。

一个包可以同时拥有多个 `implementation variant`。它们按语言等价，而不按主次排列。下游总是依赖自己所需语言对应的 `exit file`。如果并列变体还没有被 `equivalence contract` 和 `conformance suite` 收住，就不要把它们当成稳定包结构。

三个最小例子有助于把这个模型落稳。它们一起说明一件事：`wrappers`、`tests` 和 `optional surfaces` 都按对象需要出现，不是默认全都有。

只有业务区的包，结构对象可以写成：

```json
{
  "package_root": "packages/rules",
  "package_language": ["rule", "decision"],
  "implementation_variants": [
    {"language": "go", "suffix": "go"}
  ],
  "with_wrappers": false,
  "with_tests": false,
  "fixed_point_sets": {
    "business": {
      "exit": ["src/business/exit/rule.go"]
    }
  },
  "optional_surfaces": []
}
```

带翻译边界的包，结构对象可以写成：

```json
{
  "package_root": "packages/inventory-sync",
  "package_language": ["stock", "allocation", "reservation"],
  "implementation_variants": [
    {"language": "go", "suffix": "go"},
    {"language": "ts", "suffix": "ts"}
  ],
  "with_wrappers": true,
  "with_tests": true,
  "fixed_point_sets": {
    "wrappers": {
      "entry": [
        "src/wrappers/entry/connect.go",
        "src/wrappers/entry/connect.ts"
      ],
      "exit": [
        "src/wrappers/exit/session.go",
        "src/wrappers/exit/session.ts"
      ]
    },
    "business": {
      "exit": [
        "src/business/exit/open_proxy.go",
        "src/business/exit/open_proxy.ts"
      ]
    },
    "tests": {
      "exit": [
        "src/tests/exit/proxy_conformance.go",
        "src/tests/exit/proxy_conformance.ts"
      ]
    }
  },
  "translation_boundary": {
    "exists": true,
    "upstream": ["inventory-sdk"],
    "goal": "translate sdk language into package language"
  },
  "equivalence_contract_artifact": "temp/packages/inventory-sync/equivalence.md",
  "optional_surfaces": []
}
```

附属面较多的包，结构对象可以写成：

```json
{
  "package_root": "packages/audit-sync",
  "package_language": ["audit-event", "timeline"],
  "implementation_variants": [
    {"language": "rs", "suffix": "rs"}
  ],
  "with_wrappers": true,
  "with_tests": false,
  "fixed_point_sets": {
    "wrappers": {
      "entry": ["src/wrappers/entry/load.rs"],
      "exit": ["src/wrappers/exit/timeline.rs"]
    },
    "business": {
      "exit": ["src/business/exit/export_timeline.rs"]
    }
  },
  "optional_surfaces": ["docs/", "scripts/", "fixtures/"]
}
```

最小包结构工件包含一棵树和一个结构对象：`tree.txt` 与 `structure.json`。`structure.json` 写下面这些字段：

```json
{
  "package_root": "packages/example",
  "package_language": ["proxy session", "service pool"],
  "implementation_variants": [
    {"language": "go", "suffix": "go"},
    {"language": "ts", "suffix": "ts"}
  ],
  "with_wrappers": true,
  "with_tests": true,
  "fixed_point_sets": {
    "wrappers": {
      "entry": [],
      "exit": []
    },
    "business": {
      "exit": []
    },
    "tests": {
      "exit": []
    }
  },
  "translation_boundary": {
    "exists": true,
    "upstream": ["inventory-sdk", "payment-service"],
    "goal": "translate upstream language into package language"
  },
  "optional_surfaces": [],
  "equivalence_contract_artifact": "temp/packages/example/equivalence.md"
}
```

这个对象最先停在目标仓库自己的 `temp/packages/<package-name>/`。脚手架默认按这个落点写出工件，不相对当前执行目录漂移。若 `package_root` 不是常见的包集合子路径，显式传入 `--repository-root`，让脚手架能回到正确仓库根。若 `implementation_variants` 多于一个，再补一份：

```text
temp/packages/<package-name>/equivalence.md
```

这份文件至少写三件事：

1. 哪些 `implementation variant` 被视为等价变体。
2. 它们共享的出入口职责是什么。
3. 需要靠哪组 `conformance suite` 继续核对一致性。

脚手架的最小输入也不接受空默认值。至少显式传入：

1. 一个非空的 `package_language`
2. 至少一个 `implementation variant`
3. 至少一个 `business/exit` 文件
4. 若出现 `wrappers`，再传 `translation_upstream`、`translation_goal`、`wrappers entry` 和 `wrappers exit` 文件集合
5. 若出现 `tests`，再传 `tests/exit` 文件集合

写第一份结构工件时，补三句自然语言说明：

1. 这个包承接的单一需求边界是什么。
2. 这个包的统一语言是什么。
3. 哪些语义区出现了，为什么出现。

把“脚本输入 -> 结构工件 -> 文件落点”串成一轮最小例子，长相如下：

```text
input:
- package_root=packages/inventory-sync
- implementation_variants=[go, ts]
- package_language=[stock, allocation, reservation]
- with_wrappers=true
- with_tests=true
- wrappers entry=[connect.go, connect.ts]
- wrappers exit=[session.go, session.ts]
- business exit=[open_proxy.go, open_proxy.ts]
- tests exit=[proxy_conformance.go, proxy_conformance.ts]
```

```text
output files:
- packages/inventory-sync/src/wrappers/entry/connect.go
- packages/inventory-sync/src/wrappers/entry/connect.ts
- packages/inventory-sync/src/wrappers/exit/session.go
- packages/inventory-sync/src/wrappers/exit/session.ts
- packages/inventory-sync/src/business/exit/open_proxy.go
- packages/inventory-sync/src/business/exit/open_proxy.ts
- packages/inventory-sync/src/tests/exit/proxy_conformance.go
- packages/inventory-sync/src/tests/exit/proxy_conformance.ts
- temp/packages/inventory-sync/tree.txt
- temp/packages/inventory-sync/structure.json
- temp/packages/inventory-sync/equivalence.md
```

这轮动作的意义不是“脚本已经决定了包模型”，而是说明一旦包模型已经站住，脚本如何把它落成确定性骨架。对象判断先发生，结构工件随后跟上，文件才最后被建立。

包结构站住以后，包内关键文件的最小内容也要立刻补上。下面这些样板不依赖具体语言语法，它们描述的是每个文件最少要承接什么。

`src/wrappers/entry/<file>`

```text
1. 只承接接入边界
2. 不依赖 wrappers 区内任何源码文件
3. 让外部世界在这里进入当前包
```

`src/wrappers/exit/<file>`

```text
1. 只承接封装区公开边界
2. 不依赖 wrappers/entry
3. 不依赖 wrappers 区外源码文件
```

`src/business/exit/<file>`

```text
1. 只承接业务区公开边界
2. 直接依赖的 business 非出口文件数要可核对
3. 不依赖 business 区外源码文件
```

`src/tests/exit/<file>`

```text
1. 只承接测试区公开边界
2. 不依赖 tests 区外源码文件
3. 对外暴露需要复用的验证出口
```
