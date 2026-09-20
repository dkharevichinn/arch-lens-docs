# medianTypes

<!-- report-chip: median types -->

| Field | Value |
|---|---|
| `metrics.json` | `medianTypes` (number; half-integers possible) |
| Metrics chip | **median types** |
| Related finding | [C1](../findings/C1.md) uses this as the scale |

## What it measures

Median of `moduleSize[m].types` across scored modules. Even N uses the mean of the two middle values.

## How to read it

The typical module’s type count. [C1](../findings/C1.md) fires when a module is ≥ 20 types **and** ≥ 3× this median. Empty graph → 0.

## What "bad" looks like

A tiny median (many emptyish modules) plus one blob makes C1 easy to trip — sometimes correctly (the blob is real), sometimes because you split too far. A huge median means C1 may never fire (3× median is enormous); then [C4](../findings/C4.md)/[maxTypes](maxTypes.md) matter more.
