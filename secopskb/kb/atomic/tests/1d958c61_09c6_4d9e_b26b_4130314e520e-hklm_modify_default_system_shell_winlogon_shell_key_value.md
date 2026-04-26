---
atomic_guid: "1d958c61-09c6-4d9e-b26b-4130314e520e"
title: "HKLM - Modify default System Shell - Winlogon Shell KEY Value "
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "1d958c61-09c6-4d9e-b26b-4130314e520e"
  - "HKLM - Modify default System Shell - Winlogon Shell KEY Value "
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HKLM - Modify default System Shell - Winlogon Shell KEY Value 

This test change the default value of HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell from "explorer.exe" to the full path of "C:\Windows\explorer.exe" 
to log a change to the key's default value without breaking boot sequence. 
An atacker will alternatively replace this with a custom shell.

## Metadata

- Atomic GUID: 1d958c61-09c6-4d9e-b26b-4130314e520e
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Input Arguments

### payload

- description: what to run
- type: string
- default: C:\Windows\explorer.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell");
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell-backup" -Value "$oldvalue";
$newvalue = $oldvalue + ", #{payload}";
Set-ItemProperty -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell" -Value "$newvalue"
```

### Cleanup

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name 'Shell-backup');
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Shell" -Value "$oldvalue";
Remove-ItemProperty -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name 'Shell-backup'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
