---
title: "Pixtool.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Pixtool.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Pixtool.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Pixtool.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Pixtool.exe

Command line utility for taking and analyzing PIX GPU captures.

## Metadata

- Category: OtherMSBinaries
- Created: 2025-09-21
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/Pixtool.yml

## Paths

- `C:\Program Files\Microsoft PIX\pixtool.exe`
- `C:\Program Files (x86)\Microsoft PIX\pixtool.exe`

## Commands

### 1. Execute

Launches an executable via PIX command-line utility.

```cmd
pixtool.exe launch {PATH_ABSOLUTE:.exe}
```

- Use Case: Executes an executable under a trusted, Microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Resources

- {'Link': 'https://devblogs.microsoft.com/pix/pixtool/'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Pixtool.yml)
