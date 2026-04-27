---
atomic_guid: "ae4b6361-b5f8-46cb-a3f9-9cf108ccfe7b"
title: "Enumerate all accounts via PowerShell (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "ae4b6361-b5f8-46cb-a3f9-9cf108ccfe7b"
  - "Enumerate all accounts via PowerShell (Local)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerate all accounts via PowerShell. Upon execution, lots of user account and group information will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]

## Executor

- name: powershell

### Command

```powershell
net user
get-localuser
get-localgroupmember -group Users
cmdkey.exe /list
ls C:/Users
get-childitem C:\Users\
dir C:\Users\
get-localgroup
net localgroup
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
