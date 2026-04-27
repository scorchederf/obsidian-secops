---
title: "Expand.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Expand.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Expand.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Expand.exe"
functions:
  - "Download"
  - "Copy"
  - "ADS"
attack_technique_ids:
  - "T1105"
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Expand.exe

Binary that expands one or more compressed files

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Expand.yml

## Paths

- `C:\Windows\System32\Expand.exe`
- `C:\Windows\SysWOW64\Expand.exe`

## Commands

### 1. Download

Copies source file to destination.

```cmd
expand {PATH_SMB:.bat} {PATH_ABSOLUTE:.bat}
```

- Use Case: Use to copies the source file to the destination file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Copy

Copies source file to destination.

```cmd
expand {PATH_ABSOLUTE:.source.ext} {PATH_ABSOLUTE:.dest.ext}
```

- Use Case: Copies files from A to B
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 3. ADS

Copies source file to destination Alternate Data Stream (ADS)

```cmd
expand {PATH_SMB:.bat} {PATH_ABSOLUTE}:file.bat
```

- Use Case: Copies files from A to B
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_expand_cabinet_files.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml

## Resources

- {'Link': 'https://twitter.com/infosecn1nja/status/986628482858807297'}
- {'Link': 'https://twitter.com/Oddvarmoe/status/986709068759949319'}

## Acknowledgements

- {'Person': 'Rahmat Nurfauzi', 'Handle': '@infosecn1nja'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Expand.yml)
