---
title: "Sigverif.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Sigverif.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Sigverif.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Sigverif.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

File Signature Verification utility to verify digital signatures of files

## Paths

- `C:\Windows\System32\sigverif.exe`
- `C:\Windows\SysWOW64\sigverif.exe`

## Commands

### 1. Execute

Launch sigverif.exe GUI, click 'Advanced', specify arbitrary executable path as 'log file name', then click 'View Log' to execute the binary.

```cmd
sigverif.exe
```

- Use Case: Execute arbitrary programs through a trusted Microsoft-signed binary to bypass application whitelisting.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- IOC: sigverif.exe spawning unexpected child processes

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1457676633809330184'}
- {'Link': 'https://www.hexacorn.com/blog/2018/04/27/i-shot-the-sigverif-exe-the-gui-based-lolbin/'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}
- {'Person': 'Adam', 'Handle': '@Hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Sigverif.yml)
