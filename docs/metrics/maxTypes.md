# maxTypes

<!-- report-chip: max types -->

| Field | Value |
|---|---|
| `metrics.json` | `maxTypes` (int) |
| Metrics chip | **max types** |
| Related finding | [C1](../findings/C1.md) |

## What it measures

Maximum `types` among scored modules.

## How to read it

The size of the current blob. Pair with [medianTypes](medianTypes.md) and the Modules table.

## What "bad" looks like

`maxTypes` many times the median, especially ≥ 20. One module absorbing all new work ([C4](../findings/C4.md)). Not gated by itself except through C1’s predicate.
