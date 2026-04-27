---
title: "VSIISExeLauncher.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/VSIISExeLauncher.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VSIISExeLauncher.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "VSIISExeLauncher.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# VSIISExeLauncher.exe

Binary will execute specified binary. Part of VS/VScode installation.

## Metadata

- Category: OtherMSBinaries
- Created: 2021-09-24
- Author: timwhite
- Source Path: yml/OtherMSBinaries/VSIISExeLauncher.yml

## Paths

- `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Web Tools\ProjectSystem\VSIISExeLauncher.exe`

## Commands

### 1. Execute

The above binary will execute other binary.

```cmd
VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
```

- Use Case: Execute any binary with given arguments.
- Privileges: User
- Operating System: Windows 10 and up with VS/VScode installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml
- IOC: VSIISExeLauncher.exe spawned an unknown process

## Resources

- {'Link': 'https://github.com/timwhitez'}

## Acknowledgements

- {'Person': 'timwhite'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VSIISExeLauncher.yml)
