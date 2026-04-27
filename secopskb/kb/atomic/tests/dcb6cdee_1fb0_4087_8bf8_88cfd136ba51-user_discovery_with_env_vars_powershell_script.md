---
atomic_guid: "dcb6cdee-1fb0-4087-8bf8-88cfd136ba51"
title: "User Discovery With Env Vars PowerShell Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "dcb6cdee-1fb0-4087-8bf8-88cfd136ba51"
  - "User Discovery With Env Vars PowerShell Script"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use the PowerShell environment variables to identify the current logged user.

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]

## Executor

- name: powershell

### Command

```powershell
[System.Environment]::UserName | Out-File -FilePath .\CurrentactiveUser.txt 
$env:UserName | Out-File -FilePath .\CurrentactiveUser.txt -Append
```

### Cleanup

```powershell
Remove-Item -Path .\CurrentactiveUser.txt -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
