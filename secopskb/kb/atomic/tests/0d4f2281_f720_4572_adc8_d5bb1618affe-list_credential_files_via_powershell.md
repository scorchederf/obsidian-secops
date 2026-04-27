---
atomic_guid: "0d4f2281-f720-4572-adc8-d5bb1618affe"
title: "List Credential Files via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-27 19:12:28"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Via PowerShell,list files where credentials are stored in Windows Credential Manager

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

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
