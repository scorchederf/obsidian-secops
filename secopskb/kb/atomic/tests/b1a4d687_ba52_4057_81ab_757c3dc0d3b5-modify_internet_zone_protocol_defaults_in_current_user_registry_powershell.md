---
atomic_guid: "b1a4d687-ba52-4057-81ab-757c3dc0d3b5"
title: "Modify Internet Zone Protocol Defaults in Current User Registry - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b1a4d687-ba52-4057-81ab-757c3dc0d3b5"
  - "Modify Internet Zone Protocol Defaults in Current User Registry - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify Internet Zone Protocol Defaults in Current User Registry - PowerShell

This test simulates an adversary modifying the Internet Zone Protocol Defaults in the registry of the currently logged-in user using PowerShell. Such modifications can be indicative of an adversary attempting to weaken browser security settings. 
To verify the effects of the test:
1. Open the Registry Editor (regedit.exe).
2. Navigate to "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults".
3. Check for the presence of the "http" and "https" DWORD values set to `0`.
Or run:
```powershell
Get-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' | Select-Object http,https
```

## Metadata

- Atomic GUID: b1a4d687-ba52-4057-81ab-757c3dc0d3b5
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: powershell

### Command

```powershell
# Set the registry values for http and https to 0
Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' -Name 'http' -Value 0
Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' -Name 'https' -Value 0
```

### Cleanup

```powershell
# Restore the registry values for http and https to 3
Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' -Name 'http' -Value 3
Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults' -Name 'https' -Value 3
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
