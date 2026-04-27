---
title: "Reset.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Reset.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Reset.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Reset.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Remote Desktop Services Reset Utility

## Paths

- `c:\windows\system32\reset.exe`
- `c:\windows\syswow64\reset.exe`

## Commands

### 1. Execute

Once executed, `reset.exe` will execute `rwinsta.exe` in the same folder. Thus, if `reset.exe` is copied to a folder and an arbitrary executable is renamed to `rwinsta.exe`, `reset.exe` will spawn it.

```cmd
reset.exe session
```

- Use Case: Execute an arbitrary executable via trusted system executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- IOC: reset.exe being executed and executes rwinsta.exe outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\

## Acknowledgements

- {'Person': 'Matan Bahar', 'Handle': '@Bl4ckShad3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Reset.yml)
