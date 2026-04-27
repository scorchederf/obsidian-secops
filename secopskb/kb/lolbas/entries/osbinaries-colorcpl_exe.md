---
title: "Colorcpl.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Colorcpl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Colorcpl.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Colorcpl.exe"
functions:
  - "Copy"
attack_technique_ids:
  - "T1036.005"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Colorcpl.exe

Binary that handles color management

## Metadata

- Category: OSBinaries
- Created: 2023-06-26
- Author: Arjan Onwezen
- Source Path: yml/OSBinaries/Colorcpl.yml

## Paths

- `C:\Windows\System32\colorcpl.exe`
- `C:\Windows\SysWOW64\colorcpl.exe`

## Commands

### 1. Copy

Copies the referenced file to C:\Windows\System32\spool\drivers\color\.

```cmd
colorcpl {PATH}
```

- Use Case: Copies file(s) to a subfolder of a generally trusted folder (c:\Windows\System32), which can be used to hide files or make them blend into the environment.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml
- IOC: colorcpl.exe writing files

## Resources

- {'Link': 'https://twitter.com/eral4m/status/1480468728324231172'}

## Acknowledgements

- {'Person': 'eral4m', 'Handle': '@eral4m'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Colorcpl.yml)
