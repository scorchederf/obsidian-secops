---
title: "Change.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Change.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Change.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Change.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Remote Desktop Services MultiUser Change Utility

## Paths

- `c:\windows\system32\change.exe`
- `c:\windows\syswow64\change.exe`

## Commands

### 1. Execute

Once executed, `change.exe` will execute `chgusr.exe` in the same folder. Thus, if `change.exe` is copied to a folder and an arbitrary executable is renamed to `chgusr.exe`, `change.exe` will spawn it. Instead of `user`, it is also possible to use `port` or `logon` as command-line option.

```cmd
change.exe user
```

- Use Case: Execute an arbitrary executable via trusted system executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- IOC: change.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\

## Acknowledgements

- {'Person': 'Idan Lerman', 'Handle': '@IdanLerman'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Change.yml)
