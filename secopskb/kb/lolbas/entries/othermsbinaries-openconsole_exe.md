---
title: "OpenConsole.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/OpenConsole.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/OpenConsole.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "OpenConsole.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OpenConsole.exe

Console Window host for Windows Terminal

## Metadata

- Category: OtherMSBinaries
- Created: 2022-06-17
- Author: Nasreddine Bencherchali
- Source Path: yml/OtherMSBinaries/OpenConsole.yml

## Paths

- `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os86\OpenConsole.exe`
- `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe`
- `C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.18.10301.0_x64__8wekyb3d8bbwe\OpenConsole.exe`

## Commands

### 1. Execute

Execute specified process with OpenConsole.exe as parent process

```cmd
OpenConsole.exe {PATH:.exe}
```

- Use Case: Use OpenConsole.exe as a proxy binary to evade defensive counter-measures
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- IOC: OpenConsole.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/9e0ef7251b075f15e7abafbbec16d3230c5fa477/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml

## Resources

- {'Link': 'https://twitter.com/nas_bench/status/1537563834478645252'}

## Acknowledgements

- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/OpenConsole.yml)
