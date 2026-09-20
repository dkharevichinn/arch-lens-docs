# block

| Field | Value |
|---|---|
| JSON | `block` |
| Exit code | `5` (`CliExitCodes.Block`) |
| Meaning | At least one finding is class `invariant` or `ratchet` |

## When it fires

Typical blockers:

- New [A1](../findings/A1.md) / [A2](../findings/A2.md) / [A7](../findings/A7.md)
- New [B1](../findings/B1.md) cycle not in `knownCycles`
- Ratchet worse than baseline: [A3](../findings/A3.md), [A4](../findings/A4.md), [B2](../findings/B2.md), [B3](../findings/B3.md), [B4](../findings/B4.md), [B9](../findings/B9.md), [F1](../findings/F1.md)
- [G1](../findings/G1.md) violating or cycle-forming (with `--against`)

Triggers may appear in the same report; the verdict is still **block**.

## What to do

Fix the invariant or revert the ratchet (internalize types, break the cycle, point tests at contracts). Only then re-baseline if the new number is the policy floor.

## What not to do

- Do **not** rewrite `baseline.json` as the fix.
- Do **not** add `knownCycles` for a cycle you just introduced.
- Do **not** InternalsVisibleTo a product assembly to “fix” A1 ([A7](../findings/A7.md) will block instead).

See [pass](pass.md), [triggers](triggers.md).
