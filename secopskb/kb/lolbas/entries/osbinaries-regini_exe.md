---
title: "Regini.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Regini.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Regini.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Regini.exe"
functions:
  - "ADS"
attack_technique_ids:
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regini.exe

Used to manipulate the registry

## Metadata

- Category: OSBinaries
- Created: 2020-07-03
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Regini.yml

## Paths

- `C:\Windows\System32\regini.exe`
- `C:\Windows\SysWOW64\regini.exe`

## Commands

### 1. ADS

Write registry keys from data inside the Alternate data stream.

```cmd
regini.exe {PATH}:hidden.ini
```

- Use Case: Write to registry
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_execution.yml
- IOC: regini.exe reading from ADS

## Resources

- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}

## Acknowledgements

- {'Person': 'Eli Salem', 'Handle': '@elisalem9'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Regini.yml)
