# Arch Lens catalog

This site is the **human-readable catalog** of every finding code, metric, and gate verdict the Arch Lens tool emits. It is the page a later report change will deep-link to from `dsm.html` (finding codes and metric names). Those HTML links are **not** in this drop.

**This site does not replace** the design notes under [`docs/superpowers/`](https://github.com/dkharevichinn/arch-lens/tree/main/docs/superpowers) in the repository. Those specs stay in git; this site is the operator-facing catalog with examples and general-case fixes.

## Stable URLs

| Kind | Pattern | Example |
|---|---|---|
| Finding | `/findings/{code}/` | [`/findings/A1/`](findings/A1.md) |
| Metric | `/metrics/{metrics.json key}/` | [`/metrics/tanglePct/`](metrics/tanglePct.md) |
| Gate verdict | `/gates/{pass\|triggers\|block}/` | [`/gates/block/`](gates/block.md) |

Canonical metric URLs use **`metrics.json` keys** (camelCase). Metrics-tab **chip labels** (`tangle`, `shared gravity`, …) are bound on those pages so a later report can map either the chip or the JSON key.

## How findings relate to the gate

Arch Lens findings carry a **class**:

| Class (`findings.json` / `gate-report.json`) | Gate effect | Typical use |
|---|---|---|
| `invariant` | **block** (exit 5) | New illegal edges, new module cycles, InternalsVisibleTo to non-tests |
| `ratchet` | **block** (exit 5) | A number got strictly worse than `baseline.json` |
| `trigger` | **triggers** (exit 4) unless something else blocks | Smell, outlier, missing ratchet, review item |

`arch-lens gate` prints `verdict=pass|triggers|block`. See [Gate](gates/index.md).

Silencing a fingerprint in `baseline.json` `knownFindings` (or a cycle in `knownCycles`) is for **acknowledged debt**, not a substitute for a structural fix. Each finding page says when silence is legitimate and when it is hiding the problem.

## Families

| Prefix | Family | Typical class |
|---|---|---|
| A | Contracts and assembly boundaries | invariant / ratchet / trigger |
| B | Graph shape (cycles, core, Martin, shared) | invariant / ratchet / trigger |
| C | Size and growth | trigger |
| D | Cohesion | trigger |
| E | Type smells | trigger |
| F | Tests | ratchet / trigger |
| P | DSM patterns | trigger |
| G | Diff and git coupling | invariant / trigger |
| R | Runtime (DI) | trigger |

There is **no P2** in the product. A two-module cycle is [B1](findings/B1.md). Do not invent codes that analyzers do not emit.

## Commands that emit this catalog

- `arch-lens map` — snapshot findings (`findings.json`, Findings tab) plus metrics
- `arch-lens baseline` — writes ratchets, `knownFindings`, `knownCycles`
- `arch-lens gate --baseline` — synthesizes ratchets (A3/A4, B2–B4, B9, F1) and B1; passes other snapshot findings through `knownFindings`
- `arch-lens gate --against old-graph.json` — also G1–G3, C4, A8
- `arch-lens diff` — contract visuals; **does not** emit gate findings

Product metrics skip `host` and `test` assemblies except F1/F2 (test is the source).
