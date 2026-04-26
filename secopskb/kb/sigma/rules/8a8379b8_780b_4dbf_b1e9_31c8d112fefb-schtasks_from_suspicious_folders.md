---
sigma_id: "8a8379b8-780b-4dbf-b1e9-31c8d112fefb"
title: "Schtasks From Suspicious Folders"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_folder_combos.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_folder_combos.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8a8379b8-780b-4dbf-b1e9-31c8d112fefb"
  - "Schtasks From Suspicious Folders"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Schtasks From Suspicious Folders

Detects scheduled task creations that have suspicious action command and folder combinations

## Metadata

- Rule ID: 8a8379b8-780b-4dbf-b1e9-31c8d112fefb
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-15
- Modified: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_folder_combos.yml

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
selection_create:
  CommandLine|contains: ' /create '
selection_command:
  CommandLine|contains:
  - powershell
  - pwsh
  - 'cmd /c '
  - 'cmd /k '
  - 'cmd /r '
  - 'cmd.exe /c '
  - 'cmd.exe /k '
  - 'cmd.exe /r '
selection_all_folders:
  CommandLine|contains:
  - C:\ProgramData\
  - '%ProgramData%'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/lazarus-dream-job-chemical

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_folder_combos.yml)
