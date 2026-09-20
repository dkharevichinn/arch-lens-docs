# cohesion

<!-- report-table: Cohesion -->

| Field | Value |
|---|---|
| `metrics.json` | `cohesion` (object module → `{ h, islands }`) |
| Report table | **Cohesion** |
| Related findings | [D1](../findings/D1.md), [D2](../findings/D2.md) |

## What it measures

Only modules with **≥ 4 types** appear.

- `h` = `(R + 1) / N` with `R` internal type-edge weight
- `islands` = weakly connected component count on undirected internal edges

## How to read it

Healthy `h` in **[1.5, 4]**. `islands == 1` means one blob of collaboration. [D2](../findings/D2.md) needs a second island of size ≥ 3, not merely `islands ≥ 2`.

Modules with 1–3 types are omitted (no row).

## What "bad" looks like

`h < 1.5` (bag of types) or `h > 4` (clique / god cluster). `islands` high with a large second component — split the module.
