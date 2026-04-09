# Repository Construction Terminology

| 术语 | 状态 | 定义 | 边界 | 备注 |
| --- | --- | --- | --- | --- |
| `repository root` | `formal` | 仓库顶层入口与仓库级事实所在的位置 | 不等于所有实现面，也不等于任意顶层目录集合 | 共享词；主定义见 ../../terminology-governance/references/TERMINOLOGY.md |
| `bounded context` | `formal` | 围绕同一问题边界和统一语言成立的工作范围 | 不等于“完全没有依赖” | 包在这里按这种对象理解 |
| `package root` | `formal` | 围绕单一需求边界建立的包级承接对象 | 不只是目录容器 | 共享词；主定义见 ../../terminology-governance/references/TERMINOLOGY.md |
| `core structure` | `formal` | 为了站住对象边界、统一语言和公开边界而必须拥有的结构 | 不等于任意可选目录集合 | 结构判断主词 |
| `optional surfaces` | `formal` | 按对象需要增加、但不替代核心结构的附属面 | 不等于结构必有项 | 允许为空 |
| `active package set` | `formal` | 当前仍承接活需求的一组包对象 | 不等于仓库里所有目录 | 后续演化对象 |
| `package language` | `formal` | 当前包内部业务判断所使用的统一语言 | 不等于上游依赖语言 | 由 `business` 承接 |
| `compositional upstream dependency` | `formal` | 会把外来语言带入当前包，且当前包公开能力部分由其构成的上游依赖 | 不包括纯工具性依赖 | 决定 `wrappers` 是否出现 |
| `translation boundary` | `formal` | 把上游语言翻译成包语言的边界对象 | 不负责重定义业务边界 | 通常落在 `wrappers` |
| `validation surface` | `formal` | 已形成独立验证对象、验证逻辑或可复用验证出口的责任面 | 不等于“包里有测试” | 决定 `tests` 是否出现 |
| `entry file` | `formal` | 位于固定 `entry/` 目录下、承担接入边界且文件名符合 `<suffix>.<suffix>` 的文件 | 不等于任意入口命名文件 | 局部词 |
| `exit file` | `formal` | 位于固定 `exit/` 目录下、承担公开边界且文件名符合 `<suffix>.<suffix>` 的文件 | 不等于任意导出文件 | 局部词 |
| `internal source file` | `formal` | 位于语义区内、但不在固定 `entry/` 或 `exit/` 目录下的源码文件 | 不等于附属面文件 | 局部词 |
| `implementation variant` | `formal` | 同一个包边界下、以某种语言给出的等价实现变体 | 不等于新包，也不等于任意第二套实现草稿 | 共享词；主定义见 ../../terminology-governance/references/TERMINOLOGY.md |
| `equivalence contract` | `formal` | 约束同一包下多个 `implementation variant` 公开行为等价的主契约 | 不等于实现细节对齐清单 | 局部词 |
| `conformance suite` | `formal` | 用于核对多个 `implementation variant` 没有行为漂移的一组一致性检查 | 不等于任意测试集合 | 局部词 |
| `split signal` | `formal` | 说明当前包边界已写散、需要考虑拆分的结构信号 | 不等于任意复杂度增加 | 见 [DECISIONS.md](DECISIONS.md) |
| `protocol` | `formal` | 一类稳定交互的契约对象 | 不等于某个具体传输层 | 运行时建模对象 |
| `client kernel` | `formal` | 消费某个协议的一侧内核 | 不等于实例本身 | 运行时建模对象 |
| `server kernel` | `formal` | 提供某个协议的一侧内核 | 不等于实例本身 | 运行时建模对象 |
| `instance package` | `formal` | 装配若干内核并形成可运行实例的包对象 | 不等于任意实现目录 | 运行时建模对象 |
