---
atomic_guid: "0d4f2281-f720-4572-adc8-d5bb1618affe"
title: "List Credential Files via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "0d4f2281-f720-4572-adc8-d5bb1618affe"
  - "List Credential Files via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List Credential Files via PowerShell

Via PowerShell,list files where credentials are stored in Windows Credential Manager

## Metadata

- Atomic GUID: 0d4f2281-f720-4572-adc8-d5bb1618affe
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$usernameinfo = (Get-ChildItem Env:USERNAME).Value
Get-ChildItem -Hidden C:\Users\$usernameinfo\AppData\Roaming\Microsoft\Credentials\
Get-ChildItem -Hidden C:\Users\$usernameinfo\AppData\Local\Microsoft\Credentials\
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
