---
title: "Extexport.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Extexport.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Extexport.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Extexport.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Load a DLL located in the c:\test folder with a specific name.

## Paths

- `C:\Program Files\Internet Explorer\Extexport.exe`
- `C:\Program Files (x86)\Internet Explorer\Extexport.exe`

## Commands

### 1. Execute

Load a DLL located in the specified folder with one of the following names mozcrt19.dll, mozsqlite3.dll, or sqlite.dll.

```cmd
Extexport.exe {PATH_ABSOLUTE:folder} foo bar
```

- Use Case: Execute dll file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extexport.yml
- IOC: Extexport.exe loads dll and is execute from other folder the original path

## Resources

- {'Link': 'http://www.hexacorn.com/blog/2018/04/24/extexport-yet-another-lolbin/'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Extexport.yml)
