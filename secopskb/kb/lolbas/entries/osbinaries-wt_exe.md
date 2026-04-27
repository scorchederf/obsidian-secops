---
title: "wt.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/wt.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/wt.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "wt.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# wt.exe

Windows Terminal

## Metadata

- Category: OSBinaries
- Created: 2022-07-27
- Author: Nasreddine Bencherchali
- Source Path: yml/OSBinaries/wt.yml

## Paths

- `C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe`

## Commands

### 1. Execute

Execute a command via Windows Terminal.

```cmd
wt.exe {CMD}
```

- Use Case: Use wt.exe as a proxy binary to evade defensive counter-measures
- Privileges: User
- Operating System: Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml

## Resources

- {'Link': 'https://twitter.com/nas_bench/status/1552100271668469761'}

## Acknowledgements

- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/wt.yml)
