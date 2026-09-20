# coreShare

<!-- report-chip: coreShare -->

| Field | Value |
|---|---|
| `metrics.json` | `coreShare` (number 0–1) |
| Metrics chip | **coreShare** (percent) |
| Related finding | [B5](../findings/B5.md) |

## What it measures

`|largest cyclic SCC| / |scored modules|`, or 0 if there is no cyclic SCC.

## How to read it

Chip is percent. A 3-module core in a 12-module system is `0.25`. Independent of the B5 threshold (B5 uses **absolute** core size).

## What "bad" looks like

The core eating a large fraction of modules: a “middle” that everything must cycle through. Even a 2-cycle in a 2-module repo is `coreShare = 1` — read with [coreSize](coreSize.md) and N.
