---
sigma_id: "85d23b42-9a9d-4f8f-b3d7-d2733c1d58f5"
title: "HackTool - HollowReaper Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_hollowreaper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hollowreaper.yml"
build_date: "2026-04-26 14:14:26"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "85d23b42-9a9d-4f8f-b3d7-d2733c1d58f5"
  - "HackTool - HollowReaper Execution"
attack_technique_ids:
  - "T1055.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - HollowReaper Execution

Detects usage of HollowReaper, a process hollowing shellcode launcher used for stealth payload execution through process hollowing.
It replaces the memory of a legitimate process with custom shellcode, allowing the attacker to execute payloads under the guise of trusted binaries.

## Metadata

- Rule ID: 85d23b42-9a9d-4f8f-b3d7-d2733c1d58f5
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-07-01
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_hollowreaper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.012]]

## Detection

```yaml
selection:
  Image|endswith: \HollowReaper.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/vari-sh/RedTeamGrimoire/tree/b5e7635d34db6e1f0398d8847e8f293186e947c5/HollowReaper

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hollowreaper.yml)
