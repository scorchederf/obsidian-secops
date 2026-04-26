---
sigma_id: "7a02e22e-b885-4404-b38b-1ddc7e65258a"
title: "Suspicious Schtasks Schedule Type With High Privileges"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_schedule_type_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_type_system.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7a02e22e-b885-4404-b38b-1ddc7e65258a"
  - "Suspicious Schtasks Schedule Type With High Privileges"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Schtasks Schedule Type With High Privileges

Detects scheduled task creations or modification to be run with high privileges on a suspicious schedule type

## Metadata

- Rule ID: 7a02e22e-b885-4404-b38b-1ddc7e65258a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-31
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_schedule_type_system.yml

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
selection_privs:
  CommandLine|contains:
  - NT AUT
  - ' SYSTEM'
  - HIGHEST
condition: all of selection_*
```

## False Positives

- Some installers were seen using this method of creation unfortunately. Filter them in your environment

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-change
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_type_system.yml)
