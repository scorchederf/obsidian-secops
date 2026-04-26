---
sigma_id: "7c0dcd3d-acf8-4f71-9570-f448b0034f94"
title: "PsExec Service Child Process Execution as LOCAL SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc_as_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc_as_system.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7c0dcd3d-acf8-4f71-9570-f448b0034f94"
  - "PsExec Service Child Process Execution as LOCAL SYSTEM"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PsExec Service Child Process Execution as LOCAL SYSTEM

Detects suspicious launch of the PSEXESVC service on this system and a sub process run as LOCAL_SYSTEM (-s), which means that someone remotely started a command on this system running it with highest privileges and not only the privileges of the login user account (e.g. the administrator account)

## Metadata

- Rule ID: 7c0dcd3d-acf8-4f71-9570-f448b0034f94
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc_as_system.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage: C:\Windows\PSEXESVC.exe
  User|contains:
  - AUTHORI
  - AUTORI
condition: selection
```

## False Positives

- Users that debug Microsoft Intune issues using the commands mentioned in the official documentation; see https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc_as_system.yml)
