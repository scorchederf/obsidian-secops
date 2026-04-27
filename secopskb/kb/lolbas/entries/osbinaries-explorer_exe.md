---
title: "Explorer.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Explorer.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Explorer.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Explorer.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Explorer.exe

Binary used for managing files and system components within Windows

## Metadata

- Category: OSBinaries
- Created: 2020-06-24
- Author: Jai Minton
- Source Path: yml/OSBinaries/Explorer.yml

## Paths

- `C:\Windows\explorer.exe`
- `C:\Windows\SysWOW64\explorer.exe`

## Commands

### 1. Execute

Execute specified .exe with the parent process spawning from a new instance of explorer.exe

```cmd
explorer.exe /root,"{PATH_ABSOLUTE:.exe}"
```

- Use Case: Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense evasion.
- Privileges: User
- Operating System: Windows XP, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. Execute

Execute notepad.exe with the parent process spawning from a new instance of explorer.exe

```cmd
explorer.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense evasion.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_lolbin_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f2bc0c685d83db7db395fc3dc4b9729759cd4329/rules/windows/initial_access_via_explorer_suspicious_child_parent_args.toml
- IOC: Multiple instances of explorer.exe or explorer.exe using the /root command line is suspicious.

## Resources

- {'Link': 'https://twitter.com/CyberRaiju/status/1273597319322058752?s=20'}
- {'Link': 'https://twitter.com/bohops/status/1276356245541335048'}
- {'Link': 'https://twitter.com/bohops/status/986984122563391488'}

## Acknowledgements

- {'Person': 'Jai Minton', 'Handle': '@CyberRaiju'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Explorer.yml)
