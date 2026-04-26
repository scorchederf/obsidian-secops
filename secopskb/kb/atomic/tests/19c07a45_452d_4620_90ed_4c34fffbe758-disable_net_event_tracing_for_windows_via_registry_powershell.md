---
atomic_guid: "19c07a45-452d-4620-90ed-4c34fffbe758"
title: "Disable .NET Event Tracing for Windows Via Registry (powershell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable .NET Event Tracing for Windows Via Registry (powershell)

Disables ETW for the .NET Framework using PowerShell to update the Windows registry

## Metadata

- Atomic GUID: 19c07a45-452d-4620-90ed-4c34fffbe758
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

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
