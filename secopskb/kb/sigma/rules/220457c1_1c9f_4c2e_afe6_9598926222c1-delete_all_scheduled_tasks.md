---
sigma_id: "220457c1-1c9f-4c2e-afe6-9598926222c1"
title: "Delete All Scheduled Tasks"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_delete_all.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_delete_all.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "220457c1-1c9f-4c2e-afe6-9598926222c1"
  - "Delete All Scheduled Tasks"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete All Scheduled Tasks

Detects the usage of schtasks with the delete flag and the asterisk symbol to delete all tasks from the schedule of the local computer, including tasks scheduled by other users.

## Metadata

- Rule ID: 220457c1-1c9f-4c2e-afe6-9598926222c1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_delete_all.yml

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
  - ' /delete '
  - /tn \*
  - ' /f'
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-delete

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_delete_all.yml)
