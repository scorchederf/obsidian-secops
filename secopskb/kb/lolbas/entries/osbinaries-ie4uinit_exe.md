---
title: "Ie4uinit.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ie4uinit.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ie4uinit.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Ie4uinit.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes commands from a specially prepared ie4uinit.inf file.

## Paths

- `c:\windows\system32\ie4uinit.exe`
- `c:\windows\sysWOW64\ie4uinit.exe`
- `c:\windows\system32\ieuinit.inf`
- `c:\windows\sysWOW64\ieuinit.inf`

## Commands

### 1. Execute

Executes commands from a specially prepared ie4uinit.inf file.

```cmd
ie4uinit.exe -BaseSettings
```

- Use Case: Get code execution by copy files to another location
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- IOC: ie4uinit.exe copied outside of %windir%
- IOC: ie4uinit.exe loading an inf file (ieuinit.inf) from outside %windir%
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml

## Resources

- {'Link': 'https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ie4uinit.yml)
