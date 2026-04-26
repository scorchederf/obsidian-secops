---
atomic_guid: "8e81d090-0cd6-4d46-863c-eec11311298f"
title: "Modify Event Log Channel Access Permissions via Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "8e81d090-0cd6-4d46-863c-eec11311298f"
  - "Modify Event Log Channel Access Permissions via Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify Event Log Channel Access Permissions via Registry - PowerShell

This test simulates an adversary modifying access permissions for a Windows Event Log Channel by altering the "ChannelAccess" registry value. Specifically, it changes the Security Descriptor Definition Language (SDDL) string. These modifications can restrict or grant access to specific users or groups, potentially aiding in defense evasion by controlling who can view or modify a event log channel.
Upon execution, the user shouldn't be able to access the event log channel via the event viewer or via utilities such as "Get-EventLog" or "wevtutil".

## Metadata

- Atomic GUID: 8e81d090-0cd6-4d46-863c-eec11311298f
- Technique: T1562.002: Impair Defenses: Disable Windows Event Logging
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.002/T1562.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Input Arguments

### ChannelPath

- description: Path to the event log service channel to alter
- type: string
- default: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-TaskScheduler/Operational

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty -Path #{ChannelPath} -Name "ChannelAccess" -Value "O:SYG:SYD:(D;;0x1;;;WD)"
Restart-Service -Name EventLog -Force -ErrorAction Ignore
```

### Cleanup

```powershell
Set-ItemProperty -Path #{ChannelPath} -Name "ChannelAccess" -Value "O:BAG:SYD:(A;;0x2;;;S-1-15-2-1)(A;;0x2;;;S-1-15-3-1024-3153509613-960666767-3724611135-2725662640-12138253-543910227-1950414635-4190290187)(A;;0xf0007;;;SY)(A;;0x7;;;BA)(A;;0x7;;;SO)(A;;0x3;;;IU)(A;;0x3;;;SU)(A;;0x3;;;S-1-5-3)(A;;0x3;;;S-1-5-33)(A;;0x1;;;S-1-5-32-573)"
Restart-Service -Name EventLog -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
