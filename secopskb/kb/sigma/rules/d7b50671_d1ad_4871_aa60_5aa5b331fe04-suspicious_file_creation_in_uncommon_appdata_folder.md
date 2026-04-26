---
sigma_id: "d7b50671-d1ad-4871-aa60-5aa5b331fe04"
title: "Suspicious File Creation In Uncommon AppData Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_new_files_in_uncommon_appdata_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_new_files_in_uncommon_appdata_folder.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "d7b50671-d1ad-4871-aa60-5aa5b331fe04"
  - "Suspicious File Creation In Uncommon AppData Folder"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Creation In Uncommon AppData Folder

Detects the creation of suspicious files and folders inside the user's AppData folder but not inside any of the common and well known directories (Local, Romaing, LocalLow). This method could be used as a method to bypass detection who exclude the AppData folder in fear of FPs

## Metadata

- Rule ID: d7b50671-d1ad-4871-aa60-5aa5b331fe04
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-05
- Modified: 2023-02-23
- Source Path: rules/windows/file/file_event/file_event_win_new_files_in_uncommon_appdata_folder.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains: \AppData\
  TargetFilename|endswith:
  - .bat
  - .cmd
  - .cpl
  - .dll
  - .exe
  - .hta
  - .iso
  - .lnk
  - .msi
  - .ps1
  - .psm1
  - .scr
  - .vbe
  - .vbs
filter_main:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains:
  - \AppData\Local\
  - \AppData\LocalLow\
  - \AppData\Roaming\
condition: selection and not filter_main
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_new_files_in_uncommon_appdata_folder.yml)
