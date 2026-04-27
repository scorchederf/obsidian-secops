---
title: "Pcwrun.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Pcwrun.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pcwrun.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Pcwrun.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Program Compatibility Wizard

## Paths

- `C:\Windows\System32\pcwrun.exe`

## Commands

### 1. Execute

Open the target .EXE file with the Program Compatibility Wizard.

```cmd
Pcwrun.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. Execute

Leverage the MSDT follina vulnerability through Pcwrun to execute arbitrary commands and binaries. Note that this specific technique will not work on a patched system with the June 2022 Windows Security update.

```cmd
Pcwrun.exe /../../$(calc).exe
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/991335019833708544'}
- {'Link': 'https://twitter.com/nas_bench/status/1535663791362519040'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}
- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pcwrun.yml)
