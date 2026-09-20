# pass

| Field | Value |
|---|---|
| JSON | `pass` |
| Exit code | `0` (`CliExitCodes.Pass`) |
| Meaning | The gate found **no** remaining findings |

## When it fires

After `GateEvaluator` applies `knownFindings`, `knownCycles`, and ratchet comparisons, the findings list is empty. Improvements vs baseline (lower tangle, smaller surface) still **pass**; they do not rewrite `baseline.json`.

`map` / `baseline` / `diff` also use exit 0 on success, but they are not this verdict. This page is **`gate` only**.

## What to do

Ship. Optionally run `arch-lens baseline` when you **intend** to lock in a better ratchet (coverage-style tighten).

## What not to do

- Do **not** assume pass means “no architecture debt”. Debt can sit in `knownFindings` / `knownCycles`.
- Do **not** skip `--against` on the factory just because baseline-only pass is green — [G1](../findings/G1.md)–[A8](../findings/A8.md) never run.

See [triggers](triggers.md), [block](block.md).
