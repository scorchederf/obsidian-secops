---
title: "OneDriveStandaloneUpdater.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/OneDriveStandaloneUpdater.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/OneDriveStandaloneUpdater.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "OneDriveStandaloneUpdater.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

OneDrive Standalone Updater

## Paths

- `C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe`
- `C:\Program Files\Microsoft OneDrive\OneDriveStandaloneUpdater.exe`
- `C:\Program Files (x86)\Microsoft OneDrive\OneDriveStandaloneUpdater.exe`

## Commands

### 1. Download

Download a file from the web address specified in `HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC`. `ODSUUpdateXMLUrlFromOC` and `UpdateXMLUrlFromOC` must be equal to non-empty string values in that same registry key. `UpdateOfficeConfigTimestamp` is a UNIX epoch time which must be set to a large QWORD such as 99999999999 (in decimal) to indicate the URL cache is good. The downloaded file will be in `%localappdata%\OneDrive\StandaloneUpdater\PreSignInSettingsConfig.json`.

```cmd
OneDriveStandaloneUpdater
```

- Use Case: Download a file from the Internet without executing any anomalous executables with suspicious arguments
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- IOC: HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC being set to a suspicious non-Microsoft controlled URL
- IOC: Reports of downloading from suspicious URLs in %localappdata%\OneDrive\setup\logs\StandaloneUpdate_*.log files
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml

## Resources

- {'Link': 'https://github.com/LOLBAS-Project/LOLBAS/pull/153'}

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/OneDriveStandaloneUpdater.yml)
