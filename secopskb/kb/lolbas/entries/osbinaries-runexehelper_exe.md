---
title: "Runexehelper.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Runexehelper.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runexehelper.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Runexehelper.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launcher process

## Paths

- `c:\windows\system32\runexehelper.exe`

## Commands

### 1. Execute

Launches the specified exe. Prerequisites: (1) diagtrack_action_output environment variable must be set to an existing, writable folder; (2) runexewithargs_output.txt file cannot exist in the folder indicated by the variable.

```cmd
runexehelper.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Executes arbitrary code
- Privileges: User
- Operating System: Windows 10, Windows 11, Windows Server 2012, Windows Server 2016, Windows Server 2019, Windows Server 2022
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml
- IOC: c:\windows\system32\runexehelper.exe is run
- IOC: Existence of runexewithargs_output.txt file

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1206692239839289344'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runexehelper.yml)
