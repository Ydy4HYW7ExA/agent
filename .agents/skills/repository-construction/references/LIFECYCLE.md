# Repository Construction Lifecycle

`repository lifecycle` 指仓库在一段时间内承接需求、扩展结构、调整包体系、清理旧结构的过程。`package lifecycle` 指单个包从出现到退役的过程。`active package set` 指当前仍承接活需求的一组包对象。`migrating package` 指已经开始迁移消费者、但还没有退出活包集合的包。`retiring package` 指已经不再承接新需求、只等待清理的包。

仓库级阶段按下面这组状态理解：

| 阶段 | 含义 |
| --- | --- |
| `forming` | 仓库根和首批包根正在建立 |
| `expanding` | 新需求进入，活包集合增加，或现有包继续扩展 |
| `restructuring` | 包体系正在拆分、合并或迁移 |
| `stabilizing` | 结构调整完成，活包集合重新稳定 |
| `shrinking` | 旧包退役，活包集合减少 |

包级阶段按下面这组状态理解：

| 阶段 | 含义 |
| --- | --- |
| `emerging` | 包刚出现，结构和语言正在站住 |
| `active` | 包稳定承接活需求 |
| `splitting` | 包已出现拆分信号，新包和迁移动作正在展开 |
| `merging` | 包正在并入另一个包或吸收别的包 |
| `migrating` | 包仍可用，但主要任务是迁移旧消费者 |
| `retiring` | 包不再承接新需求，只等待清理 |
| `retired` | 包已退出活包集合 |

仓库根的包体系状态工件默认写成：

```json
{
  "repository_stage": "forming | expanding | restructuring | stabilizing | shrinking",
  "active_packages": [],
  "migrating_packages": [],
  "retiring_packages": []
}
```

包体系演化时守住四条规则：

1. 活包集合优先于目录印象。判断一个包是否还活着，看它是否仍承接活需求。
2. 迁移状态优先于立即删除。包进入 `migrating` 或 `retiring` 阶段后，可以暂时保留目录和出口；前提是状态已经写进仓库根工件。
3. 退役结论写回仓库根。包退出活包集合后，要从 `active_packages` 中移出，并进入 `retiring_packages` 或被彻底清理。
4. 合并动作写成状态变更。包进入 `merging` 时，目标包和来源包都要写进仓库根工件，直到消费者和结构工件完成收束。
