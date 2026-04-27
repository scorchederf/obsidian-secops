---
title: "Vshadow.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Vshadow.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vshadow.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Vshadow.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Vshadow.exe

VShadow is a command-line tool that can be used to create and manage volume shadow copies.

## Metadata

- Category: OtherMSBinaries
- Created: 2023-09-06
- Author: Ayberk Halaç
- Source Path: yml/OtherMSBinaries/Vshadow.yml

## Paths

- `C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe`

## Commands

### 1. Execute

Executes specified executable from vshadow.exe.

```cmd
vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C:
```

- Use Case: Performs execution of specified executable file.
- Privileges: Administrator
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml
- IOC: vshadow.exe usage with -exec parameter

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/windows/win32/vss/vshadow-tool-and-sample'}

## Acknowledgements

- {'Person': 'Ayberk Halaç'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vshadow.yml)
