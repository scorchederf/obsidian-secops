---
sigma_id: "dbc1f800-0fe0-4bc0-9c66-292c2abe3f78"
title: "Delete Important Scheduled Task"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_delete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_delete.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "dbc1f800-0fe0-4bc0-9c66-292c2abe3f78"
  - "Delete Important Scheduled Task"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete Important Scheduled Task

Detects when adversaries stop services or processes by deleting their respective scheduled tasks in order to conduct data destructive activities

## Metadata

- Rule ID: dbc1f800-0fe0-4bc0-9c66-292c2abe3f78
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_delete.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - /delete
  - /tn
  CommandLine|contains:
  - \Windows\BitLocker
  - \Windows\ExploitGuard
  - \Windows\SystemRestore\SR
  - \Windows\UpdateOrchestrator\
  - \Windows\Windows Defender\
  - \Windows\WindowsBackup\
  - \Windows\WindowsUpdate\
condition: selection
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_delete.yml)
