# runtime

<!-- report-table: Runtime (DI) -->

| Field | Value |
|---|---|
| `metrics.json` | `runtime` object |
| Report heading | **Runtime (DI)** plus a cycle list |
| Related findings | [R1](../findings/R1.md), [R2](../findings/R2.md) |

## What it measures

DI extraction for Microsoft.Extensions.DependencyInjection:

| JSON / row | Meaning |
|---|---|
| `registrations.total` {#registrations} | All extracted registrations |
| `generic` | `AddX<TService, TImpl>` shape |
| `factory` | factory lambdas |
| `instance` | instance registrations |
| `descriptor` | raw descriptor adds |
| `opaque` | solution-local `Add*`/`TryAdd*` that is not core MEDI (bound, impl unknown) |
| `unresolved` | registration with null implementation type id |
| `ports` | distinct ports injected on **container consumer** types |
| `unboundPorts` | count of [R2](../findings/R2.md) findings |
| `resolvedEdges` | derived consumer→implementation edges |
| `interModuleWeight` | weight of those edges that cross scored modules |
| `cycles` | runtime SCCs (static ∪ binding), including those that duplicate static [B1](../findings/B1.md) |

If there are no registrations and no injections, the reporter writes the empty runtime object (zeros, no cycles).

## How to read it

`unboundPorts` should be 0 in a wired host. `opaque` > 0 means “bound but blind”. `cycles` here can be a **superset** of static cycles; [R1](../findings/R1.md) only reports cycles that are **not** already static.

The Matrix **resolve DI** toggle draws `resolvedEdges`; it does not change these numbers.

## What "bad" looks like

`unboundPorts > 0` (production will fail to resolve). `runtime.cycles` that [R1](../findings/R1.md) flags. Huge `interModuleWeight` with a mesh of feature implementations injecting each other. `opaque` covering the entire container — the catalog cannot see implementations, so R1 may be understated.
