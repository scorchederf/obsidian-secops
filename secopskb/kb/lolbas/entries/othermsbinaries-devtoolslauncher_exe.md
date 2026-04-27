---
title: "Devtoolslauncher.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Devtoolslauncher.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Devtoolslauncher.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Devtoolslauncher.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Devtoolslauncher.exe

Binary will execute specified binary. Part of VS/VScode installation.

## Metadata

- Category: OtherMSBinaries
- Created: 2019-10-04
- Author: felamos
- Source Path: yml/OtherMSBinaries/Devtoolslauncher.yml

## Paths

- `c:\windows\system32\devtoolslauncher.exe`

## Commands

### 1. Execute

The above binary will execute other binary.

```cmd
devtoolslauncher.exe LaunchForDeploy {PATH_ABSOLUTE:.exe} "{CMD:args}" test
```

- Use Case: Execute any binary with given arguments and it will call `developertoolssvc.exe`. `developertoolssvc` is actually executing the binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. Execute

The above binary will execute other binary.

```cmd
devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test
```

- Use Case: Execute any binary with given arguments.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml
- IOC: DeveloperToolsSvc.exe spawned an unknown process

## Resources

- {'Link': 'https://twitter.com/_felamos/status/1179811992841797632'}
- {'Link': 'https://www.virustotal.com/gui/file/84877a507af8b70c145777a87eaf28a8327c50a1563fe650f34572bef8a42ff6/details'}

## Acknowledgements

- {'Person': 'felamos', 'Handle': '@_felamos'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Devtoolslauncher.yml)
