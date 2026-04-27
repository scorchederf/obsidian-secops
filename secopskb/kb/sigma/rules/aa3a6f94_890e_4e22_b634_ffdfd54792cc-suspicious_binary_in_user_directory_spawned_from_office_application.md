---
sigma_id: "aa3a6f94-890e-4e22-b634-ffdfd54792cc"
title: "Suspicious Binary In User Directory Spawned From Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_spawn_exe_from_users_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_spawn_exe_from_users_directory.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "aa3a6f94-890e-4e22-b634-ffdfd54792cc"
  - "Suspicious Binary In User Directory Spawned From Office Application"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Binary In User Directory Spawned From Office Application

Detects an executable in the users directory started from one of the Microsoft Office suite applications (Word, Excel, PowerPoint, Publisher, Visio)

## Metadata

- Rule ID: aa3a6f94-890e-4e22-b634-ffdfd54792cc
- Status: test
- Level: high
- Author: Jason Lynch
- Date: 2019-04-02
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_office_spawn_exe_from_users_directory.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \WINWORD.EXE
  - \EXCEL.EXE
  - \POWERPNT.exe
  - \MSPUB.exe
  - \VISIO.exe
  - \MSACCESS.exe
  - \EQNEDT32.exe
  Image|startswith: C:\users\
  Image|endswith: .exe
filter:
  Image|endswith: \Teams.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://blog.morphisec.com/fin7-not-finished-morphisec-spots-new-campaign
- https://www.virustotal.com/gui/file/23160972c6ae07f740800fa28e421a81d7c0ca5d5cab95bc082b4a986fbac57

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_spawn_exe_from_users_directory.yml)
