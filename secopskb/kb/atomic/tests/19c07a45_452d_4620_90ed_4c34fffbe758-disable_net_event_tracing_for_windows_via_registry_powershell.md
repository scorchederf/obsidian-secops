---
atomic_guid: "19c07a45-452d-4620-90ed-4c34fffbe758"
title: "Disable .NET Event Tracing for Windows Via Registry (powershell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "19c07a45-452d-4620-90ed-4c34fffbe758"
  - "Disable .NET Event Tracing for Windows Via Registry (powershell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables ETW for the .NET Framework using PowerShell to update the Windows registry

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path HKLM:\Software\Microsoft\.NETFramework -Name ETWEnabled -Value 0 -PropertyType "DWord" -Force
```

### Cleanup

```powershell
REG DELETE HKLM\Software\Microsoft\.NETFramework /v ETWEnabled /f > $null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
