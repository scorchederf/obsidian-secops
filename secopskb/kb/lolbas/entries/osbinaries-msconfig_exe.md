---
title: "Msconfig.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Msconfig.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msconfig.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Msconfig.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

MSConfig is a troubleshooting tool which is used to temporarily disable or re-enable software, device drivers or Windows services that run during startup process to help the user determine the cause of a problem with Windows

## Paths

- `C:\Windows\System32\msconfig.exe`

## Commands

### 1. Execute

Executes command embeded in crafted c:\windows\system32\mscfgtlc.xml.

```cmd
Msconfig.exe -5
```

- Use Case: Code execution using Msconfig.exe
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_uac_bypass_msconfig_gui.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml
- IOC: mscfgtlc.xml changes in system32 folder

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/991314564896690177'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msconfig.yml)
