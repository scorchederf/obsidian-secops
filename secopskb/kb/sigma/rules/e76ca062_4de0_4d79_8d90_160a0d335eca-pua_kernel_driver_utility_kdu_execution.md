---
sigma_id: "e76ca062-4de0-4d79-8d90-160a0d335eca"
title: "PUA - Kernel Driver Utility (KDU) Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_kdu_driver_tool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_kdu_driver_tool.yml"
build_date: "2026-04-26 17:03:20"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e76ca062-4de0-4d79-8d90-160a0d335eca"
  - "PUA - Kernel Driver Utility (KDU) Execution"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PUA - Kernel Driver Utility (KDU) Execution

Detects execution of the Kernel Driver Utility (KDU) tool.
KDU can be used to bypass driver signature enforcement and load unsigned or malicious drivers into the Windows kernel.
Potentially allowing for privilege escalation, persistence, or evasion of security controls.

## Metadata

- Rule ID: e76ca062-4de0-4d79-8d90-160a0d335eca
- Status: experimental
- Level: high
- Author: Matt Anderson, Dray Agha, Anna Pham (Huntress)
- Date: 2026-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_pua_kdu_driver_tool.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \kdu.exe
  - \hamakaze.exe
- OriginalFileName: hamakaze.exe
selection_cli_suspicious:
  CommandLine|contains:
  - '-map '
  - '-prv '
  - '-dse '
  - '-ps '
condition: all of selection_*
```

## False Positives

- Legitimate driver development, testing, or administrative troubleshooting (e.g., enabling/disabling hardware)

## References

- https://github.com/h4rmy/KDU
- https://huntress.com/blog/esxi-vm-escape-exploit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_kdu_driver_tool.yml)
