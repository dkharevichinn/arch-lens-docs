# sharedGravity

<!-- report-chip: shared gravity -->

| Field | Value |
|---|---|
| `metrics.json` | `sharedGravity` (number 0–1) |
| Metrics chip | **shared gravity** (percent) |
| Related finding | [B9](../findings/B9.md) |

## What it measures

Fraction of inter-module weight whose **target** is a `shared` module.

## How to read it

Chip is percent; JSON is a fraction. Moderate gravity is normal (everyone uses `EmailAddress`). Growth means more of the system’s coupling is aimed at the kernel.

## What "bad" looks like

Monotone increase vs baseline (**block**). A “shared” assembly that is really a feature magnet. Pair with [sharedTypeCount](sharedTypeCount.md): gravity can rise from heavier edges even if type count is flat.
