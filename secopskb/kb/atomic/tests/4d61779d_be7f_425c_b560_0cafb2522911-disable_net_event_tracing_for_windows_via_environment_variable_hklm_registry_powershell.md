---
atomic_guid: "4d61779d-be7f-425c-b560-0cafb2522911"
title: "Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "4d61779d-be7f-425c-b560-0cafb2522911"
  - "Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables ETW for the .NET Framework by setting the COMPlus_ETWEnabled environment variable to 0 in the HKLM registry using PowerShell. In order for changes to take effect a reboot might be required.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" -Name COMPlus_ETWEnabled -Value 0 -PropertyType "String" -Force
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" -Name COMPlus_ETWEnabled
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
