---
title: "Regasm.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Regasm.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Regasm.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Regasm.exe"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218.009"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Part of .NET

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\regasm.exe`
- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\regasm.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe`

## Commands

### 1. AWL Bypass

Loads the target .NET DLL file and executes the RegisterClass function.

```cmd
regasm.exe {PATH:.dll}
```

- Use Case: Execute code and bypass Application whitelisting
- Privileges: Local Admin
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218009-regsvcs-regasm|T1218.009: Regsvcs/Regasm]]

### 2. Execute

Loads the target .DLL file and executes the UnRegisterClass function.

```cmd
regasm.exe /U {PATH:.dll}
```

- Use Case: Execute code and bypass Application whitelisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218009-regsvcs-regasm|T1218.009: Regsvcs/Regasm]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_regasm.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
- Splunk: https://github.com/splunk/security_content/blob/bc93e670f5dcb24e96fbe3664d6bcad92df5acad/docs/_stories/suspicious_regsvcs_regasm_activity.md
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_regasm_with_network_connection.yml
- IOC: regasm.exe executing dll file

## Resources

- {'Link': 'https://pentestlab.blog/2017/05/19/applocker-bypass-regasm-and-regsvcs/'}
- {'Link': 'https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/'}
- {'Link': 'https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.md'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Regasm.yml)
