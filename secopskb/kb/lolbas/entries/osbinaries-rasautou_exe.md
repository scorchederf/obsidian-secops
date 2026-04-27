---
title: "Rasautou.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Rasautou.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rasautou.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Rasautou.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Rasautou.exe

Windows Remote Access Dialer

## Metadata

- Category: OSBinaries
- Created: 2020-01-10
- Author: Tony Lambert
- Source Path: yml/OSBinaries/Rasautou.yml

## Paths

- `C:\Windows\System32\rasautou.exe`

## Commands

### 1. Execute

Loads the target .DLL specified in -d and executes the export specified in -p. Options removed in Windows 10.

```cmd
rasautou -d {PATH:.dll} -p export_name -a a -e e
```

- Use Case: Execute DLL code
- Privileges: User, Administrator in Windows 8
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_rasautou_dll_execution.yml
- IOC: rasautou.exe command line containing -d and -p

## Resources

- {'Link': 'https://github.com/fireeye/DueDLLigence'}
- {'Link': 'https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html'}

## Acknowledgements

- {'Person': 'FireEye', 'Handle': '@FireEye'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rasautou.yml)
