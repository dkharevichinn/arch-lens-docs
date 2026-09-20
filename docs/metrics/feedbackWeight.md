# feedbackWeight

<!-- report-chip: feedback -->

| Field | Value |
|---|---|
| `metrics.json` | `feedbackWeight` (int) |
| Metrics chip | **feedback** |
| Related finding | [B3](../findings/B3.md) |

## What it measures

Sum of inter-module edge weights that point **against** the Eades–Lin–Smyth layer order (the same order the DSM can use for “dependency layers”). Those cells sit above the diagonal in a well-layered matrix.

## How to read it

An integer weight, not a percent. `0` means the heuristic found no back edges. Compare to baseline, not to an absolute universal scale — a large repo has larger numbers.

## What "bad" looks like

The number **grows** ([B3](../findings/B3.md) blocks). Many red/back cells on the matrix after ordering by layers. Shared depending on features, or UI depending “up” into another feature’s body, shows up here even before a full [B1](../findings/B1.md) cycle.
