# Metrics

Canonical pages use **`metrics.json` property names**. Report chips and tables are bound with HTML comments so a later `dsm.html` change can map labels without guessing.

Header chips on the Matrix tab (`components`, `dependencies`, `weight`, language, generated, commit) are report chrome, not architecture metrics. They are not catalogued here.

## Chips (Metrics tab)

| Chip label | `metrics.json` key | Page |
|---|---|---|
| tangle | `tanglePct` | [tanglePct](tanglePct.md) |
| feedback | `feedbackWeight` | [feedbackWeight](feedbackWeight.md) |
| propagation | `propagationCost` | [propagationCost](propagationCost.md) |
| shared gravity | `sharedGravity` | [sharedGravity](sharedGravity.md) |
| shared types | `sharedTypeCount` | [sharedTypeCount](sharedTypeCount.md) |
| median types | `medianTypes` | [medianTypes](medianTypes.md) |
| max types | `maxTypes` | [maxTypes](maxTypes.md) |
| median loc | `medianLoc` | [medianLoc](medianLoc.md) |
| max loc | `maxLoc` | [maxLoc](maxLoc.md) |
| coreShare | `coreShare` | [coreShare](coreShare.md) |
| coreSize | `coreSize` | [coreSize](coreSize.md) |
| maxModulePath | `maxModulePath` | [maxModulePath](maxModulePath.md) |
| testsPastContract | `testsPastContract` | [testsPastContract](testsPastContract.md) |

## Tables

| Report heading | Primary key | Page |
|---|---|---|
| Cycles | `cycles` | [cycles](cycles.md) |
| Runtime (DI) | `runtime` | [runtime](runtime.md) |
| Modules | `moduleSize` (+ fan-in/out, public impl) | [moduleSize](moduleSize.md) |
| Contracts | `contractSurface` | [contractSurface](contractSurface.md) |
| Martin | `martin` | [martin](martin.md) |
| Cohesion | `cohesion` | [cohesion](cohesion.md) |
| Layer LOC | `layerLoc` | [layerLoc](layerLoc.md) |

Per-module maps that are JSON-only (no dedicated heading of their own besides Modules / chips): [fanInOut](fanInOut.md), [publicInImplementation](publicInImplementation.md).

Role-group headings on the Metrics tab (`snapshot.Modules.Groups`) are the YAML/convention module catalog, not a `metrics.json` key.

Host and test assemblies are omitted from product metrics unless a rule uses test as the source ([F1](../findings/F1.md) / [F2](../findings/F2.md)).
