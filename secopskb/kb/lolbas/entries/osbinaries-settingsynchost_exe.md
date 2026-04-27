---
title: "SettingSyncHost.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/SettingSyncHost.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/SettingSyncHost.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "SettingSyncHost.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Host Process for Setting Synchronization

## Paths

- `C:\Windows\System32\SettingSyncHost.exe`
- `C:\Windows\SysWOW64\SettingSyncHost.exe`

## Commands

### 1. Execute

Execute file specified in %COMSPEC%

```cmd
SettingSyncHost -LoadAndRunDiagScript {PATH:.exe}
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: User
- Operating System: Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. Execute

Execute a batch script in the background (no window ever pops up) which can be subverted to running arbitrary programs by setting the current working directory to %TMP% and creating files such as reg.bat/reg.exe in that directory thereby causing them to execute instead of the ones in C:\Windows\System32.

```cmd
SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat}
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism. Additionally, effectively act as a -WindowStyle Hidden option (as there is in PowerShell) for any arbitrary batch file.
- Privileges: User
- Operating System: Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_settingsynchost.yml
- IOC: SettingSyncHost.exe should not be run on a normal workstation

## Resources

- {'Link': 'https://www.hexacorn.com/blog/2020/02/02/settingsynchost-exe-as-a-lolbin/'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@hexacorn'}
- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/SettingSyncHost.yml)
