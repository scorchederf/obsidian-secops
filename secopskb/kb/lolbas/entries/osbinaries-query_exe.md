---
title: "Query.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Query.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Query.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Query.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Query.exe

Remote Desktop Services MultiUser Query Utility

## Metadata

- Category: OSBinaries
- Created: 2025-07-31
- Author: Idan Lerman
- Source Path: yml/OSBinaries/Query.yml

## Paths

- `c:\windows\system32\query.exe`
- `c:\windows\syswow64\query.exe`

## Commands

### 1. Execute

Once executed, `query.exe` will execute `quser.exe` in the same folder. Thus, if `query.exe` is copied to a folder and an arbitrary executable is renamed to `quser.exe`, `query.exe` will spawn it. Instead of `user`, it is also possible to use `session`, `termsession` or `process` as command-line option.

```cmd
query.exe user
```

- Use Case: Execute an arbitrary executable via trusted system executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- IOC: query.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\

## Acknowledgements

- {'Person': 'Idan Lerman', 'Handle': '@IdanLerman'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Query.yml)
