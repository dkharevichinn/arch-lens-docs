# triggers

| Field | Value |
|---|---|
| JSON | `triggers` |
| Exit code | `4` (`CliExitCodes.Triggers`) |
| Meaning | At least one finding remains, and **none** are `invariant` or `ratchet` |

## When it fires

The leftover list is only class `trigger`: smells (E*), cohesion (D*), outliers (B5–B8, C*, P*), runtime (R*), F2, G2/G3/G4, A5/A6/A8, new-module A3/A4, missing F1 ratchet, etc.

CI should **fail or route to analysis**, not merge as if the graph were clean. The factory design uses exit 4 as “AI/human review”, not “ignore”.

## What to do

Read each trigger page, fix the real structure, or **explicitly** add fingerprints to `knownFindings` for accepted debt. New dictionary-key A3/A4/F1 triggers usually mean “run baseline after review”.

## What not to do

- Do **not** treat 4 as 0 in the pipeline.
- Do **not** bulk-copy `findings.json` fingerprints into baseline without reading them.
- Do **not** disable analyzers or raise thresholds to convert a noisy triggers run into pass.

See [pass](pass.md), [block](block.md).
