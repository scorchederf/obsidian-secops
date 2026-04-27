---
title: "devtunnel.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/devtunnels.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/devtunnels.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "devtunnel.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# devtunnel.exe

Binary to enable forwarded ports on windows operating systems.

## Metadata

- Category: OtherMSBinaries
- Created: 2023-09-16
- Author: Kamran Saifullah
- Source Path: yml/OtherMSBinaries/devtunnels.yml

## Paths

- `C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe`
- `C:\Users\<username>\AppData\Local\Temp\DevTunnels\devtunnel.exe`

## Commands

### 1. Download

Enabling a forwarded port for locally hosted service at port 8080 to be exposed on the internet.

```cmd
devtunnel.exe host -p 8080
```

- Use Case: Download Files, Upload Files, Data Exfiltration
- Privileges: User
- Operating System: Windows 10, Windows 11, MacOS
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
- IOC: devtunnel.exe binary spawned
- IOC: *.devtunnels.ms
- IOC: *.*.devtunnels.ms
- Analysis: https://cydefops.com/vscode-data-exfiltration

## Resources

- {'Link': 'https://code.visualstudio.com/docs/editor/port-forwarding'}

## Acknowledgements

- {'Person': 'Kamran Saifullah', 'Handle': '@deFr0ggy'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/devtunnels.yml)
