---
title: "Eudcedit.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Eudcedit.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Eudcedit.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Eudcedit.exe"
functions:
  - "UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Private Character Editor Windows Utility

## Paths

- `c:\windows\system32\eudcedit.exe`
- `c:\windows\syswow64\eudcedit.exe`

## Commands

### 1. UAC Bypass

Once executed, the Private Charecter Editor will be opened - click OK, then click File -> Font Links. In the next window choose the option "Link with Selected Fonts" and click on Save As, then in the opened enter the command you want to execute.

```cmd
eudcedit
```

- Use Case: Execute a binary or script as a high-integrity process without a UAC prompt.
- Privileges: Administrator
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detections

- IOC: Processes spawned by eudcedit.exe.

## Resources

- {'Link': 'https://medium.com/@matanb707/windows-fonts-exploitation-in-2025-bypassing-uac-with-eudcedit-915599705639'}

## Acknowledgements

- {'Person': 'Matan Bahar', 'Handle': '@Bl4ckShad3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Eudcedit.yml)
