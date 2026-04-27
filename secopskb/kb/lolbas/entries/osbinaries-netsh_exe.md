---
title: "Netsh.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Netsh.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Netsh.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Netsh.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1546.007"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Netsh is a Windows tool used to manipulate network interface settings.

## Paths

- `C:\WINDOWS\System32\Netsh.exe`
- `C:\WINDOWS\SysWOW64\Netsh.exe`

## Commands

### 1. Execute

Use Netsh in order to execute a .dll file and also gain persistence, every time the netsh command is called

```cmd
netsh.exe add helper {PATH_ABSOLUTE:.dll}
```

- Use Case: Proxy execution of .dll
- Privileges: Admin
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/processes_launching_netsh.yml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/deprecated/processes_created_by_netsh.yml
- IOC: Netsh initiating a network connection

## Resources

- {'Link': 'https://freddiebarrsmith.com/trix/trix.html'}
- {'Link': 'https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html'}
- {'Link': 'https://liberty-shell.com/sec/2018/07/28/netshlep/'}

## Acknowledgements

- {'Person': 'Freddie Barr-Smith', 'Handle': None}
- {'Person': 'Riccardo Spolaor', 'Handle': None}
- {'Person': 'Mariano Graziano', 'Handle': None}
- {'Person': 'Xabier Ugarte-Pedrero', 'Handle': None}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Netsh.yml)
