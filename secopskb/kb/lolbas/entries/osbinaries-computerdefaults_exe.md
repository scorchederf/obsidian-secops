---
title: "ComputerDefaults.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/ComputerDefaults.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/ComputerDefaults.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "ComputerDefaults.exe"
functions:
  - "UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ComputerDefaults.exe is a Windows system utility for managing default applications for tasks like web browsing, emailing, and media playback.

## Paths

- `C:\Windows\System32\ComputerDefaults.exe`
- `C:\Windows\SysWOW64\ComputerDefaults.exe`

## Commands

### 1. UAC Bypass

Upon execution, ComputerDefaults.exe checks two registry values at HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command; if these are set by an attacker, the set command will be executed as a high-integrity process without a UAC prompt being displayed to the user. See 'resources' for which registry keys/values to set.

```cmd
ComputerDefaults.exe
```

- Use Case: Execute a binary or script as a high-integrity process without a UAC prompt.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detections

- IOC: Event ID 10
- IOC: A binary or script spawned as a child process of ComputerDefaults.exe
- IOC: Changes to HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml

## Resources

- {'Link': 'https://gist.github.com/havoc3-3/812547525107bd138a1a839118a3a44b'}

## Acknowledgements

- {'Person': 'Eron Clarke'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/ComputerDefaults.yml)
