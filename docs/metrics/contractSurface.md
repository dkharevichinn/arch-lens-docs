# contractSurface

<!-- report-table: Contracts -->

| Field | Value |
|---|---|
| `metrics.json` | `contractSurface` (object **assembly** → int) |
| Report table | **Contracts** (Unit, Surface) |
| Related findings | [A4](../findings/A4.md), [A8](../findings/A8.md), [G2](../findings/G2.md) |

## What it measures

Per **contract assembly** (not module id): public type count + sum of `PublicMembers` on those public types.

Assemblies without a contract role do not appear. Empty object if the repo has no contract assemblies.

## How to read it

The Contracts table **Unit** column is the assembly name (`Account.Contracts`). **Surface** is the integer. Gate ratchet keys must match those names.

## What "bad" looks like

Surface growing every PR ([A4](../findings/A4.md) blocks). A huge surface with [C2](../findings/C2.md) anemic (many contract types, little body). Shrinking surface is not A4; disappearing members with `--against` are [A8](../findings/A8.md).
