---
atomic_guid: "39a295ca-7059-4a88-86f6-09556c1211e7"
title: "Windows - Delete Volume Shadow Copies via WMI with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "39a295ca-7059-4a88-86f6-09556c1211e7"
  - "Windows - Delete Volume Shadow Copies via WMI with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows - Delete Volume Shadow Copies via WMI with PowerShell

Deletes Windows Volume Shadow Copies with PowerShell code and Get-WMIObject.
This technique is used by numerous ransomware families such as Sodinokibi/REvil.
Executes Get-WMIObject. Shadow copies can only be created on Windows server or Windows 8, so upon execution
there may be no output displayed.

## Metadata

- Atomic GUID: 39a295ca-7059-4a88-86f6-09556c1211e7
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-WmiObject Win32_Shadowcopy | ForEach-Object {$_.Delete();}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
