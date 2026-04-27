---
atomic_guid: "85e6eff8-3ed4-4e03-ae50-aa6a404898a5"
title: "Modify Event Log Channel Access Permissions via Registry 2 - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "85e6eff8-3ed4-4e03-ae50-aa6a404898a5"
  - "Modify Event Log Channel Access Permissions via Registry 2 - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Event Log Channel Access Permissions via Registry 2 - PowerShell

This test simulates an adversary modifying access permissions for a Windows Event Log Channel by altering the "ChannelAccess" registry value. Specifically, it changes the Security Descriptor Definition Language (SDDL) string. These modifications can restrict or grant access to specific users or groups, potentially aiding in defense evasion by controlling who can view or modify a event log channel.
Upon execution, the user shouldn't be able to access the event log channel via the event viewer or via utilities such as "Get-EventLog" or "wevtutil".

## Metadata

- Atomic GUID: 85e6eff8-3ed4-4e03-ae50-aa6a404898a5
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
- default: HKLM:\SOFTWARE\Policies\Microsoft\Windows\EventLog\Setup

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-Item -Path #{ChannelPath} -Force
Set-ItemProperty -Path #{ChannelPath} -Name "ChannelAccess" -Value "O:SYG:SYD:(D;;0x1;;;WD)"
Restart-Service -Name EventLog -Force -ErrorAction Ignore
```

### Cleanup

```powershell
Remove-Item -Path #{ChannelPath} -Force
Restart-Service -Name EventLog -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
