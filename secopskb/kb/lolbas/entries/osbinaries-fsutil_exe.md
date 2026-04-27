---
title: "Fsutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Fsutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Fsutil.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Fsutil.exe"
functions:
  - "Tamper"
  - "Execute"
attack_technique_ids:
  - "T1485"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Fsutil.exe

File System Utility

## Metadata

- Category: OSBinaries
- Created: 2021-08-16
- Author: Elliot Killick
- Source Path: yml/OSBinaries/Fsutil.yml

## Paths

- `C:\Windows\System32\fsutil.exe`
- `C:\Windows\SysWOW64\fsutil.exe`

## Commands

### 1. Tamper

Zero out a file

```cmd
fsutil.exe file setZeroData offset=0 length=9999999999 {PATH_ABSOLUTE}
```

- Use Case: Can be used to forensically erase a file
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1485-data_destruction|T1485]]

### 2. Tamper

Delete the USN journal volume to hide file creation activity

```cmd
fsutil.exe usn deletejournal /d c:
```

- Use Case: Can be used to hide file creation activity
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1485-data_destruction|T1485]]

### 3. Execute

Executes a pre-planted binary named netsh.exe from the current directory.

```cmd
fsutil.exe trace decode
```

- Use Case: Spawn a pre-planted executable from fsutil.exe.
- Privileges: User
- Operating System: Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- IOC: fsutil.exe should not be run on a normal workstation
- IOC: file setZeroData (not case-sensitive) in the process arguments
- IOC: Sysmon Event ID 1
- IOC: Execution of process fsutil.exe with trace decode could be suspicious
- IOC: Non-Windows netsh.exe execution
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_susp_fsutil_usage.yml

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1720724516324704404'}

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Fsutil.yml)
