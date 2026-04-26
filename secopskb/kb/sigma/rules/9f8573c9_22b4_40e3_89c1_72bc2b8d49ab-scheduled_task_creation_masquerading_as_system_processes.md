---
sigma_id: "9f8573c9-22b4-40e3-89c1-72bc2b8d49ab"
title: "Scheduled Task Creation Masquerading as System Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_system_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_system_process.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9f8573c9-22b4-40e3-89c1-72bc2b8d49ab"
  - "Scheduled Task Creation Masquerading as System Processes"
attack_technique_ids:
  - "T1053.005"
  - "T1036.004"
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Creation Masquerading as System Processes

Detects the creation of scheduled tasks that involve system processes, which may indicate malicious actors masquerading as or abusing these processes to execute payloads or maintain persistence.

## Metadata

- Rule ID: 9f8573c9-22b4-40e3-89c1-72bc2b8d49ab
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_system_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1036-masquerading|T1036.004]]
- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli:
  CommandLine|contains|windash: ' /create '
  CommandLine|contains:
  - ' audiodg'
  - ' conhost'
  - ' dwm.exe'
  - ' explorer'
  - ' lsass'
  - ' lsm'
  - ' mmc'
  - ' msiexec'
  - ' regsvr32'
  - ' rundll32'
  - ' services'
  - ' spoolsv'
  - ' svchost'
  - ' taskeng'
  - ' taskhost'
  - ' wininit'
  - ' winlogon'
condition: all of selection_*
```

## False Positives

- Legitimate system administration tasks scheduling trusted system processes.

## References

- https://tria.ge/241015-l98snsyeje/behavioral2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_system_process.yml)
