---
title: "Ttdinject.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ttdinject.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ttdinject.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Ttdinject.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Ttdinject.exe

Used by Windows 1809 and newer to Debug Time Travel (Underlying call of tttracer.exe)

## Metadata

- Category: OSBinaries
- Created: 2020-05-12
- Author: Maxime Nadeau
- Source Path: yml/OSBinaries/Ttdinject.yml

## Paths

- `C:\Windows\System32\ttdinject.exe`
- `C:\Windows\Syswow64\ttdinject.exe`

## Commands

### 1. Execute

Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run. The log file can be changed, but the length (7) has to be updated.

```cmd
TTDInject.exe /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /Launch "{PATH:.exe}"
```

- Use Case: Spawn process using other binary
- Privileges: Administrator
- Operating System: Windows 10 2004 and above, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. Execute

Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run. The log file can be changed, but the length (7) has to be updated.

```cmd
ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}"
```

- Use Case: Spawn process using other binary
- Privileges: Administrator
- Operating System: Windows 10 1909 and below
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/7ea6ed3db65e0bd812b051d9bb4fffd27c4c4d0a/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml
- IOC: Parent child relationship. Ttdinject.exe parent for executed command
- IOC: Multiple queries made to the IFEO registry key of an untrusted executable (Ex. "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\payload.exe") from the ttdinject.exe process

## Resources

- {'Link': 'https://twitter.com/Oddvarmoe/status/1196333160470138880'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'Maxime Nadeau', 'Handle': '@m_nad0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ttdinject.yml)
