---
title: "Forfiles.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Forfiles.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Forfiles.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Forfiles.exe"
functions:
  - "Execute"
  - "ADS"
attack_technique_ids:
  - "T1202"
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Forfiles.exe

Selects and executes a command on a file or set of files. This command is useful for batch processing.

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Forfiles.yml

## Paths

- `C:\Windows\System32\forfiles.exe`
- `C:\Windows\SysWOW64\forfiles.exe`

## Commands

### 1. Execute

Executes specified command since there is a match for notepad.exe in the c:\windows\System32 folder.

```cmd
forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}"
```

- Use Case: Use forfiles to start a new process to evade defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. ADS

Executes the evil.exe Alternate Data Stream (AD) since there is a match for notepad.exe in the c:\windows\system32 folder.

```cmd
forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe"
```

- Use Case: Use forfiles to start a new process from a binary hidden in an alternate data stream
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_forfiles.yml

## Resources

- {'Link': 'https://twitter.com/vector_sec/status/896049052642533376'}
- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}
- {'Link': 'https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/'}

## Acknowledgements

- {'Person': 'Eric', 'Handle': '@vector_sec'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Forfiles.yml)
