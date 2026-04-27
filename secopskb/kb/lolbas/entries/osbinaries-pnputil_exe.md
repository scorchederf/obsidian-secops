---
title: "Pnputil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Pnputil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pnputil.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Pnputil.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1547"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used for installing drivers

## Paths

- `C:\Windows\system32\pnputil.exe`

## Commands

### 1. Execute

Used for installing drivers

```cmd
pnputil.exe -i -a {PATH_ABSOLUTE:.inf}
```

- Use Case: Add malicious driver
- Privileges: Administrator
- Operating System: Windows 7, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml

## Acknowledgements

- {'Person': 'Hai Vaknin(Lux)', 'Handle': '@LuxNoBulIshit'}
- {'Person': 'Avihay eldad', 'Handle': '@aloneliassaf'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pnputil.yml)
