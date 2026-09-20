# moduleSize

<!-- report-table: Modules -->

| Field | Value |
|---|---|
| `metrics.json` | `moduleSize` (object module → `{ types, loc }`) |
| Report table | **Modules** (also shows fan-in/out and public impl from other maps) |
| Related findings | [C1](../findings/C1.md), [C4](../findings/C4.md), [P3](../findings/P3.md) |

## What it measures

Per scored module, number of types and summed `Loc`. Host/test types never land here.

## How to read it

The Modules table is the operator view: size + [fanInOut](fanInOut.md) + [publicInImplementation](publicInImplementation.md). JSON `moduleSize` is only types/loc.

Medians/maxes of these columns are the chips [medianTypes](medianTypes.md), [maxTypes](maxTypes.md), [medianLoc](medianLoc.md), [maxLoc](maxLoc.md).

## What "bad" looks like

One row with types ≥ 20 and ≥ 3× median ([C1](../findings/C1.md)). A row that takes ≥ 70% of positive Δtypes ([C4](../findings/C4.md)). A row with types > 0 and both fans 0 ([P3](../findings/P3.md)).
