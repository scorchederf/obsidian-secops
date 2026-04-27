---
title: "fltMC.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/FltMC.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/FltMC.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "fltMC.exe"
functions:
  - "Tamper"
attack_technique_ids:
  - "T1562.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# fltMC.exe

Filter Manager Control Program used by Windows

## Metadata

- Category: OSBinaries
- Created: 2021-09-18
- Author: John Lambert
- Source Path: yml/OSBinaries/FltMC.yml

## Paths

- `C:\Windows\System32\fltMC.exe`

## Commands

### 1. Tamper

Unloads a driver used by security agents

```cmd
fltMC.exe unload SysmonDrv
```

- Use Case: Defense evasion
- Privileges: Admin
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_via_filter_manager.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/unload_sysmon_filter_driver.yml
- IOC: 4688 events with fltMC.exe

## Resources

- {'Link': 'https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon'}

## Acknowledgements

- {'Person': 'Carlos Perez', 'Handle': '@Carlos_Perez'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/FltMC.yml)
