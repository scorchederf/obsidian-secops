---
title: "Conhost.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Conhost.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Conhost.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Conhost.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Console Window host

## Paths

- `c:\windows\system32\conhost.exe`

## Commands

### 1. Execute

Execute a command line with conhost.exe as parent process

```cmd
conhost.exe {CMD}
```

- Use Case: Use conhost.exe as a proxy binary to evade defensive counter-measures
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Execute

Execute a command line with conhost.exe as parent process

```cmd
conhost.exe --headless {CMD}
```

- Use Case: Specify --headless parameter to hide child process window (if applicable)
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detections

- IOC: conhost.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml

## Resources

- {'Link': 'https://www.hexacorn.com/blog/2020/05/25/how-to-con-your-host/'}
- {'Link': 'https://twitter.com/Wietze/status/1511397781159751680'}
- {'Link': 'https://twitter.com/embee_research/status/1559410767564181504'}
- {'Link': 'https://twitter.com/ankit_anubhav/status/1561683123816972288'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@hexacorn'}
- {'Person': 'Wietze', 'Handle': '@wietze'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Conhost.yml)
