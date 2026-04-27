---
atomic_guid: "a0cb81f8-44d0-4ac4-a8f3-c5c7f43a12c1"
title: "Modify Event Log Access Permissions via Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a0cb81f8-44d0-4ac4-a8f3-c5c7f43a12c1"
  - "Modify Event Log Access Permissions via Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Event Log Access Permissions via Registry - PowerShell

This test simulates an adversary modifying access permissions for a Windows Event Log channel by setting the "CustomSD" registry value. Specifically, it changes the Security Descriptor Definition Language (SDDL) string. These modifications can restrict or grant access to specific users or groups, potentially aiding in defense evasion by controlling who can view or modify a event log channel.
Upon execution, the user shouldn't be able to access the event log channel via the event viewer or via utilities such as "Get-EventLog" or "wevtutil".

## Metadata

- Atomic GUID: a0cb81f8-44d0-4ac4-a8f3-c5c7f43a12c1
- Technique: T1562.002: Impair Defenses: Disable Windows Event Logging
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.002/T1562.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Input Arguments

### CustomSDPath

- description: Path to the event log service channel to alter
- type: string
- default: HKLM:\SYSTEM\CurrentControlSet\Services\EventLog\System

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty -Path #{CustomSDPath} -Name "CustomSD" -Value "O:SYG:SYD:(D;;0x1;;;WD)"
```

### Cleanup

```powershell
Remove-ItemProperty -Path #{CustomSDPath} -Name "CustomSD"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
