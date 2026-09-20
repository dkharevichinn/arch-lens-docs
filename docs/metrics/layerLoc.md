# layerLoc

<!-- report-table: Layer LOC -->

| Field | Value |
|---|---|
| `metrics.json` | `layerLoc` (object module → `{ contract, implementation, infrastructure, ui }`) |
| Report table | **Layer LOC** |
| Related findings | [C2](../findings/C2.md), [C3](../findings/C3.md) |

## What it measures

LOC summed from types, bucketed by **assembly role** inside the module. Shared/host/test types do not appear in these four buckets (host/test are not scored; shared types are not assigned to these role columns).

Every scored module gets a row (zeros if it has no types in a role).

## How to read it

Compare **ui** vs **implementation** for [C3](../findings/C3.md) (`ui > implementation` and implementation > 0). [C2](../findings/C2.md) uses **type counts**, not these LOC numbers.

## What "bad" looks like

UI column dominates implementation in a feature module (views owning the use-cases). Contract LOC huge and implementation tiny (anemic, often with C2). Infrastructure LOC huge with a one-type contract (opaque body — C2 uses types ≥ 20, but this table still shows the bulk).
