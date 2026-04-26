---
sigma_id: "b0524451-19af-4efa-a46f-562a977f792e"
title: "ShimCache Flush"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_shimcache_flush.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shimcache_flush.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b0524451-19af-4efa-a46f-562a977f792e"
  - "ShimCache Flush"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ShimCache Flush

Detects actions that clear the local ShimCache and remove forensic evidence

## Metadata

- Rule ID: b0524451-19af-4efa-a46f-562a977f792e
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-02-01
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_susp_shimcache_flush.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection1a:
  CommandLine|contains|all:
  - rundll32
  - apphelp.dll
selection1b:
  CommandLine|contains:
  - ShimFlushCache
  - '#250'
selection2a:
  CommandLine|contains|all:
  - rundll32
  - kernel32.dll
selection2b:
  CommandLine|contains:
  - BaseFlushAppcompatCache
  - '#46'
condition: ( selection1a and selection1b ) or ( selection2a and selection2b )
```

## False Positives

- Unknown

## References

- https://medium.com/@blueteamops/shimcache-flush-89daff28d15e

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shimcache_flush.yml)
