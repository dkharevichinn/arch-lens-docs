# sharedTypeCount

<!-- report-chip: shared types -->

| Field | Value |
|---|---|
| `metrics.json` | `sharedTypeCount` (int) |
| Metrics chip | **shared types** |
| Related finding | none directly (see [B9](../findings/B9.md)) |

## What it measures

Number of types whose assembly role is `shared`. Not a ratchet. Complements gravity (weight) with bulk (types).

## How to read it

A small kernel is tens of types, not hundreds. Compare over time on the Metrics tab; `gate` does not block on this integer alone.

## What "bad" looks like

Shared type count climbing every sprint while features shrink — you are centralizing a monolith into one assembly. Dumping feature types into shared to dodge [A1](../findings/A1.md)/[A6](../findings/A6.md) shows up here first.
