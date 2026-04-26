---
sigma_id: "92626ddd-662c-49e3-ac59-f6535f12d189"
title: "Scheduled Task Creation Via Schtasks.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "92626ddd-662c-49e3-ac59-f6535f12d189"
  - "Scheduled Task Creation Via Schtasks.EXE"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Creation Via Schtasks.EXE

Detects the creation of scheduled tasks by user accounts via the "schtasks" utility.

## Metadata

- Rule ID: 92626ddd-662c-49e3-ac59-f6535f12d189
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2019-01-16
- Modified: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

### Software Tags

- S0111

## Detection

```yaml
selection:
  Image|endswith: \schtasks.exe
  CommandLine|contains: ' /create '
filter_main_system_user:
  User|contains:
  - AUTHORI
  - AUTORI
filter_optional_msoffice:
  ParentImage:
  - C:\Program Files\Microsoft Office\root\integration\integrator.exe
  - C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe
  Image:
  - C:\Windows\System32\schtasks.exe
  - C:\Windows\SysWOW64\schtasks.exe
  CommandLine|contains: Microsoft\Office\Office Performance Monitor
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Administrative activity
- Software installation

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks-create

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml)
