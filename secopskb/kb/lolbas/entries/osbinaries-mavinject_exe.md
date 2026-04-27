---
title: "Mavinject.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Mavinject.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mavinject.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Mavinject.exe"
functions:
  - "Execute"
  - "ADS"
attack_technique_ids:
  - "T1218.013"
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mavinject.exe

Used by App-v in Windows

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Mavinject.yml

## Paths

- `C:\Windows\System32\mavinject.exe`
- `C:\Windows\SysWOW64\mavinject.exe`

## Commands

### 1. Execute

Inject evil.dll into a process with PID 3110.

```cmd
MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll}
```

- Use Case: Inject dll file into running process
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.013]]

### 2. ADS

Inject file.dll stored as an Alternate Data Stream (ADS) into a process with PID 4172

```cmd
Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll
```

- Use Case: Inject dll file into running process
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml
- IOC: mavinject.exe should not run unless APP-v is in use on the workstation

## Resources

- {'Link': 'https://twitter.com/gN3mes1s/status/941315826107510784'}
- {'Link': 'https://twitter.com/Hexcorn/status/776122138063409152'}
- {'Link': 'https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/'}

## Acknowledgements

- {'Person': 'Giuseppe N3mes1s', 'Handle': '@gN3mes1s'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mavinject.yml)
