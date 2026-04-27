---
sigma_id: "24c8392b-aa3c-46b7-a545-43f71657fe98"
title: "Suspicious Schtasks Schedule Types"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_schedule_type.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_type.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "24c8392b-aa3c-46b7-a545-43f71657fe98"
  - "Suspicious Schtasks Schedule Types"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Schtasks Schedule Types

Detects scheduled task creations or modification on a suspicious schedule type

## Metadata

- Rule ID: 24c8392b-aa3c-46b7-a545-43f71657fe98
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_schedule_type.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_time:
  CommandLine|contains:
  - ' ONLOGON '
  - ' ONSTART '
  - ' ONCE '
  - ' ONIDLE '
filter_privs:
  CommandLine|contains:
  - NT AUT
  - ' SYSTEM'
  - HIGHEST
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Legitimate processes that run at logon. Filter according to your environment

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-change
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create
- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_type.yml)
