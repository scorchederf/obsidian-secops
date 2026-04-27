---
title: "odbcad32.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/odbcad32.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/odbcad32.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "odbcad32.exe"
functions:
  - "UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ODBC Data Source Administrator to manage User/System DSNs and ODBC drivers.

## Paths

- `c:\windows\system32\odbcad32.exe`
- `c:\windows\syswow64\odbcad32.exe`

## Commands

### 1. UAC Bypass

Launch odbcad32.exe GUI, click 'Tracing' tab, click 'Browsing' button, enter abitrary command in the File Dialog's path, press enter.

```cmd
odbcad32.exe
```

- Use Case: Execute a binary as a high-integrity process without a UAC prompt.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detections

- IOC: odbcad32.exe spawning unexpected child processes.

## Resources

- {'Link': 'https://medium.com/@thebinaryhashira/living-off-the-land-and-living-above-uac-6a66738d225c'}

## Acknowledgements

- {'Person': 'amonitoring'}
- {'Person': 'Ekitji', 'Handle': '@eki_erk'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/odbcad32.yml)
