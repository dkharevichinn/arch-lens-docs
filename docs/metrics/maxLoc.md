# maxLoc

<!-- report-chip: max loc -->

| Field | Value |
|---|---|
| `metrics.json` | `maxLoc` (int) |
| Metrics chip | **max loc** |
| Related finding | [C1](../findings/C1.md) is types-based; this is the LOC twin on the chip row |

## What it measures

Maximum module LOC among scored modules.

## How to read it

Where the source text lives. A module can have modest type counts and still dominate LOC (generated UI, large switch tables).

## What "bad" looks like

One module’s LOC dwarfs the rest while [layerLoc](layerLoc.md) shows that bulk in UI ([C3](../findings/C3.md)) or infrastructure. Not a ratchet by itself.
