---
title: "IntelliTrace.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/IntelliTrace.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/IntelliTrace.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "IntelliTrace.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# IntelliTrace.exe

Visual Studio command-line tool for collecting and managing diagnostic trace files.

## Metadata

- Category: OtherMSBinaries
- Created: 2025-09-21
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/IntelliTrace.yml

## Paths

- `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe`

## Commands

### 1. Execute

Launches an executable via Visual Studio command line utility.

```cmd
IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
```

- Use Case: Executes an executable under a trusted microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/visualstudio/debugger/intellitrace'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/IntelliTrace.yml)
