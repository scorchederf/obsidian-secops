---
title: "Control.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Control.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Control.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Control.exe"
functions:
  - "ADS"
  - "Execute"
attack_technique_ids:
  - "T1218.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Control.exe

Binary used to launch controlpanel items in Windows

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Control.yml

## Paths

- `C:\Windows\System32\control.exe`
- `C:\Windows\SysWOW64\control.exe`

## Commands

### 1. ADS

Execute evil.dll which is stored in an Alternate Data Stream (ADS).

```cmd
control.exe {PATH_ABSOLUTE}:evil.dll
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.002]]

### 2. Execute

Execute .cpl file. A CPL is a DLL file with CPlApplet export function)

```cmd
control.exe {PATH_ABSOLUTE:.cpl}
```

- Use Case: Use to execute code and bypass application whitelisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.002]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules-emerging-threats/2021/Exploits/CVE-2021-40444/proc_creation_win_exploit_cve_2021_40444.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Elastic: https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: Control.exe executing files from alternate data streams
- IOC: Control.exe executing library file without cpl extension
- IOC: Suspicious network connections from control.exe

## Resources

- {'Link': 'https://pentestlab.blog/2017/05/24/applocker-bypass-control-panel/'}
- {'Link': 'https://www.contextis.com/resources/blog/applocker-bypass-registry-key-manipulation/'}
- {'Link': 'https://twitter.com/bohops/status/955659561008017409'}
- {'Link': 'https://docs.microsoft.com/en-us/windows/desktop/shell/executing-control-panel-items'}
- {'Link': 'https://bohops.com/2018/01/23/loading-alternate-data-stream-ads-dll-cpl-binaries-to-bypass-applocker/'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Control.yml)
