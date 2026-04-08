# Repository Construction Structure

本页涉及的术语以 [TERMINOLOGY.md](TERMINOLOGY.md) 为主落点。下文只保留影响当前结构理解的最小释义：`protocol` 指稳定交互契约；`client kernel` 与 `server kernel` 指契约两侧的内核；`instance package` 指把这些内核装配成可运行实例的包对象；`repository root` 指仓库顶层入口与仓库级事实所在的位置；`package root` 指围绕单一需求边界建立的包级承接对象；`core structure` 指为了站住对象边界、统一语言和公开边界而必须拥有的结构；`optional surfaces` 指按对象需要增加、但不替代核心结构的附属面；`package language` 指当前包内部业务判断所使用的统一语言；`implementation variant` 指同一个包边界下、以某种语言给出的等价实现变体。

仓库建设的主链沿着下面这条关系展开：

```text
user task
-> protocol
-> client kernel / server kernel
-> instance package
-> package root
-> core structure / optional surfaces
-> implementation variants
-> entry file set / exit file set / internal source files
-> file relations
-> code / comments / documents / scripts
```

这条链的意义在于防止偷步。运行关系还没站住时，先不定包；包还没站住时，先不定语义区；出入口集合还没站住时，先不定依赖规则；结构和关系还没站住时，注释、文档和脚本边界也无从判断。

结构一旦出现，就写成显式工件。

仓库根先按 `repository root`、`core structure` 和 `optional surfaces` 展开。当前方法仓库的结构树如下：

```text
repository-root/
├── AGENTS.md
├── .gitignore
├── docs/
│   ├── README.md
│   ├── architecture.md
│   └── roadmap.md
├── .agents/
│   └── skills/
├── scripts/
│   └── clean_repository_cache.py
└── temp/
```

对应的仓库根对象如下：

```json
{
  "repository_root": {
    "core": [
      "AGENTS.md",
      ".gitignore",
      "docs/",
      ".agents/skills/",
      "scripts/",
      "temp/"
    ]
  }
}
```

当前仓库把 `temp/` 视为固定顶层工作区，而不是可有可无的附属面。原因很直接：草稿工件的默认落点、活包集合工件和结构分析材料都需要一个稳定仓库级位置。被 `.gitignore` 忽略的是 `temp/` 的内容，不是它作为顶层工作区的存在。

仓库根层还需要一份活包集合工件。当前结构不扩写生命周期说明，但 `active package set` 不能悬空；它默认写成：

```json
{
  "repository_root_artifacts": [
    "temp/architecture/repository-root/tree.txt",
    "temp/architecture/repository-root/structure.json",
    "temp/architecture/repository-root/active-packages.json"
  ]
}
```

这三份工件的职责也要固定下来：

| 文件 | 职责 |
| --- | --- |
| `tree.txt` | 给出仓库根外形 |
| `structure.json` | 给出仓库根结构判断 |
| `active-packages.json` | 给出当前活包集合与迁移中的包对象 |

`active-packages.json` 的最小对象如下：

```json
{
  "active_packages": [],
  "migrating_packages": [],
  "retiring_packages": []
}
```

这份文件至少承接当前活包集合和迁移中的包对象。包体系说明可以继续厚化，但工件落点和最小对象必须先站住。

运行时模型也需要一份显式工件。它默认写成：

```json
{
  "runtime_model_artifact": "temp/architecture/runtime-model.json"
}
```

`runtime-model.json` 至少承接：

```json
{
  "edges": [
    {
      "consumer_instance": "",
      "provider_instance": "",
      "protocol": "",
      "client_kernel": "",
      "server_kernel": "",
      "instance_package": "",
      "current_location": "draft | documented_fact | code_object"
    }
  ]
}
```

包根也按 `package root`、`core structure` 和 `optional surfaces` 展开。核心结构围绕问题边界、统一语言、语义区和出入口集合成立；自由附属面按这个包自己的需要出现，例如 `docs/`、`scripts/`、`fixtures/`、`temp/`。这些路径是例子，不构成上限。

当前采用三类语义区：`wrappers`、`business`、`tests`。其中 `business` 是必有区，`wrappers` 只在存在构成性上游依赖时出现，`tests` 只在独立验证责任面成立时出现。

当前先给出一棵“展开后的包结构树”。这里的 `wrappers/`、`tests/` 和所有附属面都按条件出现，不是默认必有：

```text
package-root/
├── config/
│   ├── business/
│   ├── wrappers/     # only when with_wrappers=true
│   └── tests/        # only when with_tests=true
├── src/
│   ├── wrappers/
│   │   ├── entry/
│   │   ├── exit/
│   │   └── ...       # only when with_wrappers=true
│   ├── business/
│   │   ├── exit/
│   │   └── ...
│   └── tests/
│       ├── exit/
│       └── ...       # only when with_tests=true
├── docs/             # optional
├── scripts/          # optional
├── fixtures/         # optional
└── temp/             # optional
```

这里的 `...` 表示自由内部实现位置。它们属于同一个语义区。固定的只有 `entry/` 与 `exit/` 这两类目录；结构里只有这两类固定目录。

对应的包结构对象包含下面这些核心字段：

```json
{
  "package_root": "packages/example",
  "package_language": ["proxy session", "service pool"],
  "implementation_variants": [
    {"language": "go", "suffix": "go"},
    {"language": "ts", "suffix": "ts"}
  ],
  "with_wrappers": true,
  "with_tests": false,
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
    }
  },
  "translation_boundary": {
    "exists": true,
    "upstream": ["inventory-sdk"],
    "goal": "translate upstream language into package language"
  },
  "optional_surfaces": ["docs/", "scripts/"]
}
```

这里有三条边界必须写死。第一，`optional_surfaces` 可以是空数组；它只表示“当前显式存在的附属面”。第二，`translation_boundary` 只在 `with_wrappers=true` 时出现。第三，`equivalence_contract_artifact` 只在 `implementation_variants` 多于一个时出现。

包根结构工件默认写成两份文件：

```json
{
  "package_root_artifacts": [
    "temp/packages/<package-name>/tree.txt",
    "temp/packages/<package-name>/structure.json"
  ]
}
```

若 `implementation_variants` 多于一个，再补一份等价契约草稿：

```json
{
  "equivalence_contract_artifact": "temp/packages/<package-name>/equivalence.md"
}
```

脚手架默认把这些工件写到目标仓库自己的 `temp/packages/<package-name>/`，不是当前执行目录。若 `package_root` 不是常见的包集合子路径，显式传入 `--repository-root`，让工件仍然挂回正确仓库根。

包根里的检查对象如下：

```json
{
  "package_root_check": {
    "package_language_exists": true,
    "fixed_point_sets_exist": true,
    "optional_surfaces_are_explicit": true,
    "optional_surfaces_do_not_replace_core": true
  },
  "package_variant_check": {
    "implementation_variants_are_explicit": true,
    "equivalence_contract_is_explicit_when_needed": true
  }
}
```

若使用脚手架建立包根，最小输入约束也要写死：

```json
{
  "scaffold_requirements": {
    "package_language": "non-empty",
    "implementation_variants": "at least one",
    "business_exit_files": "at least one",
    "translation_upstream": "required when wrappers exist",
    "translation_goal": "required when wrappers exist",
    "wrappers_entry_files": "required when wrappers exist",
    "wrappers_exit_files": "required when wrappers exist",
    "tests_exit_files": "required when tests exist"
  }
}
```

把这组结构再压成更短的检查对象，就是：

```json
{
  "repository_root_check": {
    "core_exists": true,
    "temp_workspace_exists": true,
    "active_package_set_artifact_exists": true
  },
  "package_root_check": {
    "package_language_exists": true,
    "fixed_point_sets_exist": true,
    "optional_surfaces_are_explicit": true,
    "optional_surfaces_do_not_replace_core": true
  }
}
```
