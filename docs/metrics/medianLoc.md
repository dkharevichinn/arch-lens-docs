# medianLoc

<!-- report-chip: median loc -->

| Field | Value |
|---|---|
| `metrics.json` | `medianLoc` (number) |
| Metrics chip | **median loc** |
| Related finding | none directly; [C3](../findings/C3.md) uses layer LOC not this median |

## What it measures

Median of per-module **lines of code** summed from type `Loc` on scored assemblies (all roles that participate in `moduleSize`, i.e. non-host non-test).

## How to read it

Typical module bulk. Half-integers possible for even N. Complements [medianTypes](medianTypes.md) when types are small but files are huge.

## What "bad" looks like

A healthy type median with a huge LOC median (or the reverse): generated code, copy-paste, or god files. [E1](../findings/E1.md) and [C3](../findings/C3.md) tell you where the bulk sits.
