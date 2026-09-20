# propagationCost

<!-- report-chip: propagation -->

| Field | Value |
|---|---|
| `metrics.json` | `propagationCost` (number) |
| Metrics chip | **propagation** (three decimal places) |
| Related finding | [B4](../findings/B4.md) |

## What it measures

Average reachability on the directed module graph: for each start module, count reachable modules **including itself**, sum, divide by `N²`.

## How to read it

Chip format `0.000`. Lower is more tree-like. Disconnected modules give about `1/N`. A strongly connected core pushes the value toward `1`.

## What "bad" looks like

Jumps toward **1**: a change in one module can follow edges to most others. Strict increase vs baseline **blocks**. Long [B6](../findings/B6.md) paths and [B1](../findings/B1.md) cycles both inflate this.
