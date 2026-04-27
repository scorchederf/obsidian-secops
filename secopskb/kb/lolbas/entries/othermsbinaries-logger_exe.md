---
title: "Logger.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Logger.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Logger.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Logger.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A logging configuration tool from the Windows Kits used to start and manage process logging.

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\logger.exe`
- `C:\Program Files\Windows Kits\10\Debuggers\x86\logger.exe`
- `C:\Program Files\Windows Kits\10\Debuggers\x64\logger.exe`

## Commands

### 1. Execute

Executes the command specified after the `RUN` parameter as a child of `logger.exe`.

```cmd
logger.exe RUN "{CMD}"
```

- Use Case: Executes an abitrary command via a signed binary to evade detection.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Execute

Executes the command specified after the `RUNW` parameter as a child of `logger.exe`.

```cmd
logger.exe RUNW "{CMD}"
```

- Use Case: Executes an abitrary command via a signed binary to evade detection.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 3. Execute

Executes the command specified as a child of `logger.exe`.

```cmd
logger.exe "{CMD}"
```

- Use Case: Executes an abitrary command via a signed binary to evade detection.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/logger'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Logger.yml)
