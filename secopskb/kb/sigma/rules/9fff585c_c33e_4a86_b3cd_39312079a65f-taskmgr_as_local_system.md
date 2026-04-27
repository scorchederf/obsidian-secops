---
sigma_id: "9fff585c-c33e-4a86-b3cd-39312079a65f"
title: "Taskmgr as LOCAL_SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_taskmgr_localsystem.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskmgr_localsystem.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9fff585c-c33e-4a86-b3cd-39312079a65f"
  - "Taskmgr as LOCAL_SYSTEM"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Taskmgr as LOCAL_SYSTEM

Detects the creation of taskmgr.exe process in context of LOCAL_SYSTEM

## Metadata

- Rule ID: 9fff585c-c33e-4a86-b3cd-39312079a65f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-03-18
- Modified: 2022-05-27
- Source Path: rules/windows/process_creation/proc_creation_win_taskmgr_localsystem.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  User|contains:
  - AUTHORI
  - AUTORI
  Image|endswith: \taskmgr.exe
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_taskmgr_localsystem.yml)
