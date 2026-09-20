# cycles

<!-- report-table: Cycles -->

| Field | Value |
|---|---|
| `metrics.json` | `cycles` (array of arrays of module ids) |
| Report heading | **Cycles** |
| Related findings | [B1](../findings/B1.md), [B5](../findings/B5.md) |

## What it measures

Cyclic SCCs on `ModuleGraph` (size ≥ 2). Each inner array is sorted Ordinal; the outer list is sorted by joined ids.

`map` Findings tab does **not** list B1; this list (and `gate`) does.

## How to read it

Empty → `no module cycles`. Each bullet is a set that will B1-block if it is not in `knownCycles`. Runtime-only cycles are under [runtime](runtime.md), not here.

## What "bad" looks like

Any cycle in a greenfield modular monolith. Multiple overlapping cycles (a large core). `knownCycles` that never shrink.
