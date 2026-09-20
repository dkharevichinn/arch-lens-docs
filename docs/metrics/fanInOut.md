# fanInOut

| Field | Value |
|---|---|
| `metrics.json` | `fanInOut` (object module → `{ fanIn, fanOut }`) |
| Modules table | **Fan-in**, **Fan-out** |
| Related findings | [B7](../findings/B7.md), [P1](../findings/P1.md), [P3](../findings/P3.md), [B8](../findings/B8.md) |

## What it measures

`fanIn` / `fanOut` are **counts of neighboring modules**, not weights. A fat edge still counts as 1.

Every scored module appears, including zeros.

## How to read it

Fan-out ≈ “how many modules I depend on”. Fan-in ≈ “how many depend on me”. [P1](../findings/P1.md) uses **weights**, not these counts. [B7](../findings/B7.md) uses these counts vs `N`.

## What "bad" looks like

Fan-out ≈ N−1 (god row). Fan-in ≈ N−1 on a non-shared module without a contract (magnet). Both zero with types > 0 is [P3](../findings/P3.md).
