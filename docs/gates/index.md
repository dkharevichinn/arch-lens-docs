# Gate verdicts

`arch-lens gate` always returns one of three **architecture** verdicts after a successful run (usage/load/crash use exit 1–3 and are not catalogued as findings).

| Verdict | JSON | Exit | When |
|---|---|---|---|
| [pass](pass.md) | `pass` | 0 | No remaining findings |
| [triggers](triggers.md) | `triggers` | 4 | Only `trigger` class findings |
| [block](block.md) | `block` | 5 | Any `invariant` or `ratchet` finding |

`GateEvaluator` computes:

```text
if any finding.Class is Invariant or Ratchet → Block
else if any findings remain → Triggers
else → Pass
```

Snapshot findings (A1, A2, A5–A8, B5–B8, C*, D*, E*, F2, P*, G*, R*, …) pass through unless their fingerprint is in `baseline.knownFindings`. **F1 is excluded** from that loop and re-synthesized from `testsPastContract` vs the baseline ratchet.

[B1](../findings/B1.md) is synthesized from `metrics.Cycles` vs `knownCycles`, not from snapshot findings.

Ratchets [A3](../findings/A3.md), [A4](../findings/A4.md), [B2](../findings/B2.md), [B3](../findings/B3.md), [B4](../findings/B4.md), [B9](../findings/B9.md), [F1](../findings/F1.md) compare current metrics to `baseline.ratchets`. A **new dictionary key** (new module / new contract assembly) is a **trigger**, not a block.

`arch-lens map`, `baseline`, and `diff` never return 4 or 5.

## Baseline discipline

`arch-lens baseline` copies current ratchet numbers and **every current finding fingerprint** into `knownFindings`. That is how you freeze legacy debt. Rewriting baseline to make a block go away without changing code is equivalent to raising a coverage ratchet after deleting tests: do it only as an explicit policy decision.
