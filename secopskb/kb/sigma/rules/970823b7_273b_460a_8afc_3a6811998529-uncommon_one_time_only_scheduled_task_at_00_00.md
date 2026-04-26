---
sigma_id: "970823b7-273b-460a-8afc-3a6811998529"
title: "Uncommon One Time Only Scheduled Task At 00:00"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_one_time_only_midnight_task.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_one_time_only_midnight_task.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "970823b7-273b-460a-8afc-3a6811998529"
  - "Uncommon One Time Only Scheduled Task At 00:00"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon One Time Only Scheduled Task At 00:00

Detects scheduled task creation events that include suspicious actions, and is run once at 00:00

## Metadata

- Rule ID: 970823b7-273b-460a-8afc-3a6811998529
- Status: test
- Level: high
- Author: pH-T (Nextron Systems)
- Date: 2022-07-15
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_one_time_only_midnight_task.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
- Image|contains: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli:
  CommandLine|contains:
  - wscript
  - vbscript
  - cscript
  - 'wmic '
  - wmic.exe
  - regsvr32.exe
  - powershell
  - \AppData\
selection_time:
  CommandLine|contains|all:
  - once
  - 00:00
condition: all of selection_*
```

## False Positives

- Software installation

## References

- https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbyte

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_one_time_only_midnight_task.yml)
