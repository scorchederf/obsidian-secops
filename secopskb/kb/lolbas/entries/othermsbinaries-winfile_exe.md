---
title: "winfile.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/winfile.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/winfile.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "winfile.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# winfile.exe

Windows File Manager executable

## Metadata

- Category: OtherMSBinaries
- Created: 2024-04-30
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/winfile.yml

## Paths

- `C:\Windows\System32\winfile.exe`
- `C:\Windows\winfile.exe`
- `C:\Program Files\WinFile\winfile.exe`
- `C:\Program Files (x86)\WinFile\winfile.exe`
- `C:\Program Files\WindowsApps\Microsoft.WindowsFileManager_10.3.0.0_x64__8wekyb3d8bbwe\WinFile\winfile.exe`

## Commands

### 1. Execute

Execute an executable file with WinFile as a parent process.

```cmd
winfile.exe {PATH:.exe}
```

- Use Case: Performs execution of specified file, can be used as a defense evasion
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Resources

- {'Link': 'https://github.com/microsoft/winfile'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/winfile.yml)
