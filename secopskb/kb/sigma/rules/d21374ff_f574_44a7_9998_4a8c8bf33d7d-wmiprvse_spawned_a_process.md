---
sigma_id: "d21374ff-f574-44a7-9998-4a8c8bf33d7d"
title: "WmiPrvSE Spawned A Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmiprvse_spawning_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_spawning_process.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d21374ff-f574-44a7-9998-4a8c8bf33d7d"
  - "WmiPrvSE Spawned A Process"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WmiPrvSE Spawned A Process

Detects WmiPrvSE spawning a process

## Metadata

- Rule ID: d21374ff-f574-44a7-9998-4a8c8bf33d7d
- Status: stable
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-15
- Modified: 2023-03-23
- Source Path: rules/windows/process_creation/proc_creation_win_wmiprvse_spawning_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  ParentImage|endswith: \WmiPrvSe.exe
filter_logonid:
  LogonId:
  - '0x3e7'
  - 'null'
filter_system_user:
  User|contains:
  - AUTHORI
  - AUTORI
filter_wmiprvse:
  Image|endswith: \WmiPrvSE.exe
filter_werfault:
  Image|endswith: \WerFault.exe
filter_null:
  LogonId: null
condition: selection and not 1 of filter_*
```

## False Positives

- False positives are expected (e.g. in environments where WinRM is used legitimately)

## References

- https://threathunterplaybook.com/hunts/windows/190815-RemoteServiceInstallation/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_spawning_process.yml)
