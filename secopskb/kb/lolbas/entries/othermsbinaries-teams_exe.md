---
title: "Teams.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Teams.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Teams.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Teams.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.015"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Electron runtime binary which runs the Teams application

## Paths

- `C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe`

## Commands

### 1. Execute

Generate JavaScript payload and package.json, and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app\\" before executing.

```cmd
teams.exe
```

- Use Case: Execute JavaScript code
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]

### 2. Execute

Generate JavaScript payload and package.json, archive in ASAR file and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app.asar" before executing.

```cmd
teams.exe
```

- Use Case: Execute JavaScript code
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]

### 3. Execute

Teams spawns cmd.exe as a child process of teams.exe and executes the ping command

```cmd
teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

- Use Case: Executes a process under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]

## Detections

- IOC: %LOCALAPPDATA%\Microsoft\Teams\current\app directory created
- IOC: %LOCALAPPDATA%\Microsoft\Teams\current\app.asar file created/modified by non-Teams installer/updater
- Sigma: https://github.com/SigmaHQ/sigma/blob/43277f26fc1c81fc98fc79147b711189e901b757/rules/windows/process_creation/proc_creation_win_susp_electron_exeuction_proxy.yml

## Resources

- {'Link': 'https://l--k.uk/2022/01/16/microsoft-teams-and-other-electron-apps-as-lolbins/'}

## Acknowledgements

- {'Person': 'Andrew Kisliakov'}
- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Teams.yml)
