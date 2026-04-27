---
title: "Wab.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Wab.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wab.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Wab.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows address book manager

## Paths

- `C:\Program Files\Windows Mail\wab.exe`
- `C:\Program Files (x86)\Windows Mail\wab.exe`

## Commands

### 1. Execute

Change HKLM\Software\Microsoft\WAB\DLLPath and execute DLL of choice

```cmd
wab.exe
```

- Use Case: Execute dll file. Bypass defensive counter measures
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml
- IOC: WAB.exe should normally never be used

## Resources

- {'Link': 'https://twitter.com/Hexacorn/status/991447379864932352'}
- {'Link': 'http://www.hexacorn.com/blog/2018/05/01/wab-exe-as-a-lolbin/'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@Hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wab.yml)
