# maxModulePath

<!-- report-chip: maxModulePath -->

| Field | Value |
|---|---|
| `metrics.json` | `maxModulePath` (int, **edges** on the condensation DAG) |
| Metrics chip | **maxModulePath** |
| Related finding | [B6](../findings/B6.md) |

## What it measures

Longest path length in the DAG of SCCs (cycles collapsed). Not the number of modules on the path (`edges = modules - 1` on a simple chain of singletons).

## How to read it

`0` if there are no SCC nodes (empty graph). A chain of 7 modules is 6 edges — fires B6 at the default threshold 6.

## What "bad" looks like

Deep call-down through many feature modules (`UI → … → … → …`). Prefer a shallow DAG: UI/adapters → a few application modules → shared.
