---
title: "Stordiag.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Stordiag.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Stordiag.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Stordiag.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Stordiag.exe

Storage diagnostic tool

## Metadata

- Category: OSBinaries
- Created: 2021-10-21
- Author: Eral4m
- Source Path: yml/OSBinaries/Stordiag.yml

## Paths

- `c:\windows\system32\stordiag.exe`
- `c:\windows\syswow64\stordiag.exe`

## Commands

### 1. Execute

Once executed, Stordiag.exe will execute schtasks.exe systeminfo.exe and fltmc.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.

```cmd
stordiag.exe
```

- Use Case: Possible defence evasion purposes.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

Once executed, Stordiag.exe will execute schtasks.exe and powershell.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.

```cmd
stordiag.exe
```

- Use Case: Possible defence evasion purposes.
- Privileges: User
- Operating System: Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml
- IOC: systeminfo.exe, fltmc.exe or schtasks.exe or powershell.exe being executed outside of their normal path of c:\windows\system32\ or c:\windows\syswow64\

## Resources

- {'Link': 'https://twitter.com/eral4m/status/1451112385041911809'}

## Acknowledgements

- {'Person': 'Eral4m', 'Handle': '@eral4m'}
- {'Person': 'Ekitji', 'Handle': '@eki_erk'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Stordiag.yml)
