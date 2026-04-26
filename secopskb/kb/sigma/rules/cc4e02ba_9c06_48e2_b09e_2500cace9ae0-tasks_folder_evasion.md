---
sigma_id: "cc4e02ba-9c06-48e2-b09e-2500cace9ae0"
title: "Tasks Folder Evasion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_task_folder_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_task_folder_evasion.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc4e02ba-9c06-48e2-b09e-2500cace9ae0"
  - "Tasks Folder Evasion"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tasks Folder Evasion

The Tasks folder in system32 and syswow64 are globally writable paths.
Adversaries can take advantage of this and load or influence any script hosts or ANY .NET Application
in Tasks to load and execute a custom assembly into cscript, wscript, regsvr32, mshta, eventvwr

## Metadata

- Rule ID: cc4e02ba-9c06-48e2-b09e-2500cace9ae0
- Status: test
- Level: high
- Author: Sreeman
- Date: 2020-01-13
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_susp_task_folder_evasion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection1:
  CommandLine|contains:
  - 'echo '
  - 'copy '
  - 'type '
  - file createnew
selection2:
  CommandLine|contains:
  - ' C:\Windows\System32\Tasks\'
  - ' C:\Windows\SysWow64\Tasks\'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/subTee/status/1216465628946563073
- https://gist.github.com/am0nsec/8378da08f848424e4ab0cc5b317fdd26

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_task_folder_evasion.yml)
