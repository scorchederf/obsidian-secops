---
title: "WorkFolders.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/WorkFolders.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/WorkFolders.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "WorkFolders.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# WorkFolders.exe

Work Folders

## Metadata

- Category: OSBinaries
- Created: 2021-08-16
- Author: Elliot Killick
- Source Path: yml/OSBinaries/WorkFolders.yml

## Paths

- `C:\Windows\System32\WorkFolders.exe`

## Commands

### 1. Execute

Execute `control.exe` in the current working directory

```cmd
WorkFolders
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: User
- Operating System: Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

`WorkFolders` attempts to execute `control.exe`. By modifying the default value of the App Paths registry key for `control.exe` in `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\control.exe`, an attacker can achieve proxy execution.

```cmd
WorkFolders
```

- Use Case: Proxy execution of a malicious payload via App Paths registry hijacking.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_workfolders.yml
- IOC: WorkFolders.exe should not be run on a normal workstation
- IOC: Registry modification to HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\control.exe

## Resources

- {'Link': 'https://www.ctus.io/2021/04/12/exploading/'}
- {'Link': 'https://twitter.com/ElliotKillick/status/1449812843772227588'}

## Acknowledgements

- {'Person': 'John Carroll', 'Handle': '@YoSignals'}
- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}
- {'Person': 'Naor Evgi', 'Handle': '@ghosts621'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/WorkFolders.yml)
