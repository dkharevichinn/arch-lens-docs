# publicInImplementation

| Field | Value |
|---|---|
| `metrics.json` | `publicInImplementation` (object module → int) |
| Modules table column | **Public impl** |
| Related finding | [A3](../findings/A3.md) |

## What it measures

Per scored module, how many types are `public` in `implementation` or `infrastructure` assemblies. UI/contract/shared/host/test do not increment.

Every scored module key is present (0 if none).

## How to read it

The Modules table **Public impl** column is this map. JSON is the source of truth for the [A3](../findings/A3.md) ratchet. New keys on gate are triggers; increases are blocks.

## What "bad" looks like

Implementation assemblies where **everything is public**. That is an accidental API and a ratchet that will fire on every new class. Default to `internal`.
