---
title: "Pcalua.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Pcalua.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pcalua.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Pcalua.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Program Compatibility Assistant

## Paths

- `C:\Windows\System32\pcalua.exe`

## Commands

### 1. Execute

Open the target .EXE using the Program Compatibility Assistant.

```cmd
pcalua.exe -a {PATH:.exe}
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Execute

Open the target .DLL file with the Program Compatibilty Assistant.

```cmd
pcalua.exe -a {PATH_SMB:.dll}
```

- Use Case: Proxy execution of remote dll file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 3. Execute

Open the target .CPL file with the Program Compatibility Assistant.

```cmd
pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java
```

- Use Case: Execution of CPL files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml

## Resources

- {'Link': 'https://twitter.com/KyleHanslovan/status/912659279806640128'}

## Acknowledgements

- {'Person': 'Kyle Hanslovan', 'Handle': '@kylehanslovan'}
- {'Person': 'Fab', 'Handle': '@0rbz_'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pcalua.yml)
