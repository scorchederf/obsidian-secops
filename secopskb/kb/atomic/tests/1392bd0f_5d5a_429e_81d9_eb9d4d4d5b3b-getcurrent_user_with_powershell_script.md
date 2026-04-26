---
atomic_guid: "1392bd0f-5d5a-429e-81d9-eb9d4d4d5b3b"
title: "GetCurrent User with PowerShell Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1392bd0f-5d5a-429e-81d9-eb9d4d4d5b3b"
  - "GetCurrent User with PowerShell Script"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GetCurrent User with PowerShell Script

Use the PowerShell "GetCurrent" method of the WindowsIdentity .NET class to identify the logged user.

## Metadata

- Atomic GUID: 1392bd0f-5d5a-429e-81d9-eb9d4d4d5b3b
- Technique: T1033: System Owner/User Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1033/T1033.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Executor

- name: powershell

### Command

```powershell
[System.Security.Principal.WindowsIdentity]::GetCurrent() | Out-File -FilePath .\CurrentUserObject.txt
```

### Cleanup

```powershell
Remove-Item -Path .\CurrentUserObject.txt -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
