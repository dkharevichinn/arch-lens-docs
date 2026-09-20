# testsPastContract

<!-- report-chip: testsPastContract -->

| Field | Value |
|---|---|
| `metrics.json` | `testsPastContract` (number 0–1) |
| Metrics chip | **testsPastContract** (percent) |
| Related finding | [F1](../findings/F1.md) |

## What it measures

Of test→product type-edge **weight**, the fraction whose target is **not** `contract` or `shared` (implementation, infrastructure, UI). `0` if there are no test edges to scored product types.

## How to read it

Chip is percent. `0%` means tests only hit contracts/shared (or there are no test edges). `100%` means every test edge bypasses the contract.

On `map`, F1 evidence lists up to 10 heaviest past pairs. On `gate`, the number is compared to `baseline.ratchets.testsPastContract`.

## What "bad" looks like

The fraction **rising** (F1 ratchet **blocks**). Tests that new up concrete services, DbContexts, and ViewModels across modules. A missing baseline key is a **trigger**, not a silent 0.
