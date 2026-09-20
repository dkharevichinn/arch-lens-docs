# tanglePct

<!-- report-chip: tangle -->

| Field | Value |
|---|---|
| `metrics.json` | `tanglePct` (number 0–1) |
| Metrics chip | **tangle** (shown as percent) |
| Related finding | [B2](../findings/B2.md) |

## What it measures

Share of **inter-module** edge weight that sits **inside cyclic SCCs**. `cyclicWeight / totalInter`, or 0 if there is no inter-module weight.

Host/test modules are not in `ModuleGraph`, so their edges do not enter this ratio.

## How to read it

The chip is `tanglePct * 100` with a `%` suffix (e.g. `12.5%`). JSON is the fraction (`0.125`). Zero means no cyclic inter-module weight (no module cycle, or cycles with zero counted weight).

## What "bad" looks like

Rising toward **1**: almost all cross-module traffic is inside a hairball. Any increase vs `baseline.ratchets.tanglePct` **blocks** ([B2](../findings/B2.md)). A non-zero tangle with a frozen baseline is acknowledged debt — still visible on the chip.

Gaming the denominator by adding unrelated acyclic weight makes the chip look better and is not an architecture fix.
