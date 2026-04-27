---
sigma_id: "d78b5d61-187d-44b6-bf02-93486a80de5a"
title: "HackTool - DInjector PowerShell Cradle Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_dinjector.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_dinjector.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "d78b5d61-187d-44b6-bf02-93486a80de5a"
  - "HackTool - DInjector PowerShell Cradle Execution"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of the Dinject PowerShell cradle based on the specific flags

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ' /am51'
  - ' /password'
condition: selection
```

## False Positives

- Unlikely

## References

- https://web.archive.org/web/20211001064856/https://github.com/snovvcrash/DInjector

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_dinjector.yml)
