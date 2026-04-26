---
atomic_guid: "da86f239-9bd3-4e85-92ed-4a94ef111a1c"
title: "Disable EventLog-Application Auto Logger Session Via Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "da86f239-9bd3-4e85-92ed-4a94ef111a1c"
  - "Disable EventLog-Application Auto Logger Session Via Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable EventLog-Application Auto Logger Session Via Registry - PowerShell

This atomic simulates an activity where an attacker disables the EventLog-Application ETW Auto Logger session using the powershell.exe "New-ItemProperty" cmdlet to update the Windows registry value "Start". This would effectivly disable the Event log application channel. The changes would only take effect after a restart.

## Metadata

- Atomic GUID: da86f239-9bd3-4e85-92ed-4a94ef111a1c
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path HKLM:\System\CurrentControlSet\Control\WMI\Autologger\EventLog-Application -Name Start -Value 0 -PropertyType "DWord" -Force
```

### Cleanup

```powershell
New-ItemProperty -Path HKLM:\System\CurrentControlSet\Control\WMI\Autologger\EventLog-Application -Name Start -Value 1 -PropertyType "DWord" -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
