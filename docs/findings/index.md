# Findings

Every code below is emitted by `ArchLens.Analysis`. There are no extra codes on this site. Each page is the stable URL `/findings/{code}/`.

| Code | Family | Class → gate | Page |
|---|---|---|---|
| A1 | Contracts | invariant → block | [A1](A1.md) |
| A2 | Contracts | invariant → block | [A2](A2.md) |
| A3 | Contracts | trigger or ratchet | [A3](A3.md) |
| A4 | Contracts | trigger or ratchet | [A4](A4.md) |
| A5 | Contracts | trigger | [A5](A5.md) |
| A6 | Contracts | trigger | [A6](A6.md) |
| A7 | Contracts | invariant → block | [A7](A7.md) |
| A8 | Contracts | trigger (`--against`) | [A8](A8.md) |
| B1 | Graph shape | invariant → block | [B1](B1.md) |
| B2 | Graph shape | ratchet → block | [B2](B2.md) |
| B3 | Graph shape | ratchet → block | [B3](B3.md) |
| B4 | Graph shape | ratchet → block | [B4](B4.md) |
| B5 | Graph shape | trigger | [B5](B5.md) |
| B6 | Graph shape | trigger | [B6](B6.md) |
| B7 | Graph shape | trigger | [B7](B7.md) |
| B8 | Graph shape | trigger | [B8](B8.md) |
| B9 | Graph shape | ratchet → block | [B9](B9.md) |
| C1 | Size | trigger | [C1](C1.md) |
| C2 | Size | trigger | [C2](C2.md) |
| C3 | Size | trigger | [C3](C3.md) |
| C4 | Size | trigger (`--against`) | [C4](C4.md) |
| D1 | Cohesion | trigger | [D1](D1.md) |
| D2 | Cohesion | trigger | [D2](D2.md) |
| D3 | Cohesion | trigger | [D3](D3.md) |
| E1 | Type smells | trigger | [E1](E1.md) |
| E2 | Type smells | trigger | [E2](E2.md) |
| E3 | Type smells | trigger | [E3](E3.md) |
| E4 | Type smells | trigger | [E4](E4.md) |
| F1 | Tests | trigger or ratchet | [F1](F1.md) |
| F2 | Tests | trigger | [F2](F2.md) |
| P1 | DSM patterns | trigger | [P1](P1.md) |
| P3 | DSM patterns | trigger | [P3](P3.md) |
| G1 | Diff | invariant or trigger (`--against`) | [G1](G1.md) |
| G2 | Diff | trigger (`--against`) | [G2](G2.md) |
| G3 | Diff | trigger (`--against`) | [G3](G3.md) |
| G4 | Git coupling | trigger (YAML `coChange`) | [G4](G4.md) |
| R1 | Runtime | trigger | [R1](R1.md) |
| R2 | Runtime | trigger | [R2](R2.md) |

`knownFindings` swallows snapshot findings (except F1, which the gate synthesizes from the ratchet). `knownCycles` swallows [B1](B1.md) only.
