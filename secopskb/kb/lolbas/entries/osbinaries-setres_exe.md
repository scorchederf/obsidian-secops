---
title: "Setres.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Setres.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Setres.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Setres.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Configures display settings

## Paths

- `c:\windows\system32\setres.exe`

## Commands

### 1. Execute

Sets the resolution and then launches 'choice' command from the working directory.

```cmd
setres.exe -w 800 -h 600
```

- Use Case: Executes arbitrary code
- Privileges: User
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019, Windows Server 2022
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_setres.yml
- IOC: Unusual location for choice.exe file
- IOC: Process created from choice.com binary
- IOC: Existence of choice.cmd file

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1583356502340870144'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Setres.yml)
