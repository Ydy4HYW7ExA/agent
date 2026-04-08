# Repository Derivation

仓库结构如果不是从对象关系里长出来的，它很快就会沦为目录偏好。起点先摆清楚：一个问题之所以值得长成仓库结构，不是因为“看上去需要几个目录”，而是因为它已经形成了自己的问题边界、统一语言和公开边界。

问题一旦被收成新的工作范围，这个范围就按新的 `bounded context` 理解。包之所以出现，不是为了给文件找地方放，而是为了让一个问题边界拥有自己的入口、自己的统一语言、自己的内部实现区和自己的公开边界。

把这条推导压成最小关系块，就是：

```text
problem boundary
-> package root
-> package language
-> fixed entry and exit sets
-> file relations
-> explicit structure artifacts
```

这条关系块说明的不是时间顺序，而是判断依赖。前一个对象没站住，后一个对象就没有可靠落点。包语言没站住，固定出入口的职责就会浮；固定出入口没站住，文件关系表就会变成目录想象；结构工件没写出来，后续文档和脚本边界就会重新回到口头判断。

结构最后必须收成显式工件。否则分析会停留在段落或聊天里，读者仍然不知道仓库根长什么样、包根落在哪、统一语言是什么、哪些文件承担公开边界、以及多语言并列时哪些实现被视为等价。

最小落地方式，是让目标仓库至少拥有下面这组显式产物：

```json
{
  "derivation_outputs": {
    "repository_artifacts": [
      "repository root tree",
      "active package set object",
      "package root tree",
      "package language object",
      "fixed point set object",
      "implementation variant object"
    ],
    "implementation_targets": [
      "packages",
      "modules",
      "public surfaces"
    ]
  }
}
```

这样，问题边界、统一语言、出入口集合和实现变体就不会只停留在段落或临时聊天里，而会有稳定文件承接当前轮的结构判断。仓库建设真正落地的标志，不是“目录看起来像样”，而是读者能够顺着这些工件复原：当前承接的是什么对象，公开边界落在哪，哪些结构是核心，哪些只是附属面。
