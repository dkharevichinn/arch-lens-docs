# martin

<!-- report-table: Martin -->

| Field | Value |
|---|---|
| `metrics.json` | `martin` (object module → `{ instable, abstractness, distance, afferent, efferent }`) |
| Report table | **Martin** |
| Related finding | [B8](../findings/B8.md) |

## What it measures

Robert Martin I/A/D on the **module** graph:

- `afferent` = fan-in (`Ca`), `efferent` = fan-out (`Ce`)
- `instable` `I = Ce/(Ca+Ce)` (0 if unused)
- `abstractness` `A = Na/Nc` where `Na` is interfaces + abstract classes (not abstract records)
- `distance` `D = |A + I − 1|`

## How to read it

Main sequence: `A + I ≈ 1` (distance near 0). Stable (`I` low) modules should be abstract (`A` high). Unstable (`I` high) modules may be concrete.

[B8](../findings/B8.md) **pain**: no contract, `I≤0.3`, `A≤0.3`, `Ca≥2`. **concrete**: has contract and `A<0.5`.

## What "bad" looks like

Concrete hubs (low I, low A, inbound ≥ 2). Contract modules whose types are almost all concrete DTOs (`A` ≪ 0.5). Distance ~1 (maximally off the main sequence).
