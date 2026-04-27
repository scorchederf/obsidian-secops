---
title: "OfflineScannerShell.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/OfflineScannerShell.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/OfflineScannerShell.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "OfflineScannerShell.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Defender Offline Shell

## Paths

- `C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe`

## Commands

### 1. Execute

Execute mpclient.dll library in the current working directory

```cmd
OfflineScannerShell
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: Administrator
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbas_offlinescannershell.yml
- IOC: OfflineScannerShell.exe should not be run on a normal workstation

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/OfflineScannerShell.yml)
