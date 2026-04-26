---
atomic_guid: "b42c1f8c-399b-47ae-8fd8-763181395fee"
title: "Disable .NET Event Tracing for Windows Via Environment Variable HKCU Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "b42c1f8c-399b-47ae-8fd8-763181395fee"
  - "Disable .NET Event Tracing for Windows Via Environment Variable HKCU Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable .NET Event Tracing for Windows Via Environment Variable HKCU Registry - PowerShell

Disables ETW for the .NET Framework by setting the COMPlus_ETWEnabled environment variable to 0 in the HKCU registry using PowerShell. In order for changes to take effect a logout might be required.

## Metadata

- Atomic GUID: b42c1f8c-399b-47ae-8fd8-763181395fee
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Executor

- name: powershell

### Command

```powershell
New-ItemProperty -Path HKCU:\Environment -Name COMPlus_ETWEnabled -Value 0 -PropertyType "String" -Force
```

### Cleanup

```powershell
Remove-ItemProperty -Path HKCU:\Environment -Name COMPlus_ETWEnabled
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
