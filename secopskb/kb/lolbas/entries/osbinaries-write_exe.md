---
title: "write.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/write.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/write.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "write.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# write.exe

Windows Write

## Metadata

- Category: OSBinaries
- Created: 2025-06-17
- Author: Michal Belzak
- Source Path: yml/OSBinaries/write.yml

## Paths

- `C:\Windows\write.exe`
- `C:\Windows\System32\write.exe`
- `C:\Windows\SysWOW64\write.exe`

## Commands

### 1. Execute

Executes a binary provided in default value of `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe`.

```cmd
write.exe
```

- Use Case: Execute binary through legitimate proxy. This might be utilized to confuse detection solutions that rely on parent-child relationships.
- Privileges: User
- Operating System: Windows 10, Windows 11 (before 24H2)
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- IOC: Changes to HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml

## Resources

- {'Link': 'https://gist.github.com/mblzk/b8c5ff7c2bd0fb2b385cc2fdd119874b'}

## Acknowledgements

- {'Person': 'Michal Belzak'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/write.yml)
