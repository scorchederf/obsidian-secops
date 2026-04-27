---
title: "Replace.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Replace.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Replace.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Replace.exe"
functions:
  - "Copy"
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Replace.exe

Used to replace file with another file

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Replace.yml

## Paths

- `C:\Windows\System32\replace.exe`
- `C:\Windows\SysWOW64\replace.exe`

## Commands

### 1. Copy

Copy .cab file to destination

```cmd
replace.exe {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE:folder} /A
```

- Use Case: Copy files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Download

Download/Copy executable to specified folder

```cmd
replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A
```

- Use Case: Download file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- IOC: Replace.exe retrieving files from remote server
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_replace.yml

## Resources

- {'Link': 'https://twitter.com/elceef/status/986334113941655553'}
- {'Link': 'https://twitter.com/elceef/status/986842299861782529'}

## Acknowledgements

- {'Person': 'elceef', 'Handle': '@elceef'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Replace.yml)
