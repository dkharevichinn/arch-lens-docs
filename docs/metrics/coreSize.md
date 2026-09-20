# coreSize

<!-- report-chip: coreSize -->

| Field | Value |
|---|---|
| `metrics.json` | `coreSize` (int) |
| Metrics chip | **coreSize** |
| Related finding | [B5](../findings/B5.md) |

## What it measures

Number of modules in the **largest cyclic** SCC (0 if none). Ties pick the Ordinal-min joined id list.

## How to read it

`0` or `1` never appear as a cycle (singletons are not cyclic). `2` is a pair ([B1](../findings/B1.md)). `≥ gate.coreSizeMin` (default 3) emits B5.

## What "bad" looks like

Core size 5+ : a mesh, not a pair of accidentally coupled features. Do not “fix” by merging all core modules into one YAML id unless they are truly one feature.
