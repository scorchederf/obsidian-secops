---
title: "Tracker.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Tracker.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Tracker.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Tracker.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Tracker.exe

Tool included with Microsoft .Net Framework.

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Tracker.yml

## Paths

- `no default`

## Commands

### 1. Execute

Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed it can be used to bypass application whitelisting solutions.

```cmd
Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
```

- Use Case: Injection of locally stored DLL file into target process.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. AWL Bypass

Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed it can be used to bypass application whitelisting solutions.

```cmd
Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
```

- Use Case: Injection of locally stored DLL file into target process.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml

## Resources

- {'Link': 'https://twitter.com/subTee/status/793151392185589760'}
- {'Link': 'https://attack.mitre.org/wiki/Execution'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subTee'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Tracker.yml)
