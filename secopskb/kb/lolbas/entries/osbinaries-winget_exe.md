---
title: "winget.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Winget.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Winget.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "winget.exe"
functions:
  - "Execute"
  - "Download"
  - "AWL Bypass"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# winget.exe

Windows Package Manager tool

## Metadata

- Category: OSBinaries
- Created: 2022-01-03
- Author: Paul Sanders
- Source Path: yml/OSBinaries/Winget.yml

## Paths

- `C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe`

## Commands

### 1. Execute

Downloads a file from the web address specified in .yml file and executes it on the system. Local manifest setting must be enabled in winget for it to work: `winget settings --enable LocalManifestFiles`

```cmd
winget.exe install --manifest {PATH:.yml}
```

- Use Case: Download and execute an arbitrary file from the internet
- Privileges: Local Administrator - required to enable local manifest setting
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Download

Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft Store App itself is blocked on the machine. For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.

```cmd
winget.exe install --accept-package-agreements -s msstore {name or ID}
```

- Use Case: Download and install software from Microsoft Store, even if Microsoft Store App is blocked
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 3. AWL Bypass

Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft Store App itself is blocked on the machine, and even if AppLocker is active on the machine. For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.

```cmd
winget.exe install --accept-package-agreements -s msstore {name or ID}
```

- Use Case: Download and install software from Microsoft Store, even if Microsoft Store App is blocked, and AppLocker is activated on the machine
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- IOC: winget.exe spawned with local manifest file
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml

## Resources

- {'Link': 'https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html'}
- {'Link': 'https://docs.microsoft.com/en-us/windows/package-manager/winget/#production-recommended'}
- {'Link': 'https://www.youtube.com/watch?v=zuL7x4Wltto'}

## Acknowledgements

- {'Person': 'Paul', 'Handle': '@saulpanders'}
- {'Person': "Konrad 'unrooted' Klawikowski"}
- {'Person': 'Fredrik H. Brathen'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Winget.yml)
