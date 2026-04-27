---
title: "Odbcconf.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Odbcconf.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Odbcconf.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Odbcconf.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.008"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used in Windows for managing ODBC connections

## Paths

- `C:\Windows\System32\odbcconf.exe`
- `C:\Windows\SysWOW64\odbcconf.exe`

## Commands

### 1. Execute

Execute DllRegisterServer from DLL specified.

```cmd
odbcconf /a {REGSVR {PATH_ABSOLUTE:.dll}}
```

- Use Case: Execute a DLL file using technique that can evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]

### 2. Execute

Install a driver and load the DLL. Requires administrator privileges.

```cmd
odbcconf INSTALLDRIVER "lolbas-project|Driver={PATH_ABSOLUTE:.dll}|APILevel=2"
odbcconf configsysdsn "lolbas-project" "DSN=lolbas-project"
```

- Use Case: Execute dll file using technique that can evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]

### 3. Execute

Load DLL specified in target .RSP file. See the Code Sample section for an example .RSP file.

```cmd
odbcconf -f {PATH:.rsp}
```

- Use Case: Execute dll file using technique that can evade defensive counter measures
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_odbcconf_response_file_susp.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml

## Resources

- {'Link': 'https://gist.github.com/NickTyrer/6ef02ce3fd623483137b45f65017352b'}
- {'Link': 'https://github.com/woanware/application-restriction-bypasses'}
- {'Link': 'https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Adam', 'Handle': '@Hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Odbcconf.yml)
