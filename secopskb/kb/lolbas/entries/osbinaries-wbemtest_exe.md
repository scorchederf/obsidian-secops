---
title: "wbemtest.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Wbemtest.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wbemtest.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "wbemtest.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1047"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

WMI/WBEM Test Binary

## Paths

- `c:\windows\system32\wbem\wbemtest.exe`

## Commands

### 1. Execute

Execute arbitary commands through WMI through a GUI managment interface for Web Based Enterprise Management testing (WBEM). Uses WMI to Create and instance of a Win32_Process WMI class with a commandline argument of the target command to spawn. Spawns a GUI so it requires interactive access. For a demo, see link to blog in resources.

```cmd
wbemtest.exe
```

- Use Case: Execute arbitrary commands through WMI classes
- Privileges: Any
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Detections

- IOC: wbemtest.exe binary spawned

## Resources

- {'Link': 'https://saulpanders.github.io/2025/01/20/lolbas-wbemtest.html'}

## Acknowledgements

- {'Person': 'Paul Sanders', 'Handle': '@saulpanders'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wbemtest.yml)
