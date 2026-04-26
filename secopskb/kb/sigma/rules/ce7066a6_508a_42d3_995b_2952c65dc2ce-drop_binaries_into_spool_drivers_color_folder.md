---
sigma_id: "ce7066a6-508a-42d3-995b-2952c65dc2ce"
title: "Drop Binaries Into Spool Drivers Color Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_spool_drivers_color_drop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_spool_drivers_color_drop.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "ce7066a6-508a-42d3-995b-2952c65dc2ce"
  - "Drop Binaries Into Spool Drivers Color Folder"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Drop Binaries Into Spool Drivers Color Folder

Detects the creation of suspcious binary files inside the "\windows\system32\spool\drivers\color\" as seen in the blog referenced below

## Metadata

- Rule ID: ce7066a6-508a-42d3-995b-2952c65dc2ce
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-28
- Source Path: rules/windows/file/file_event/file_event_win_susp_spool_drivers_color_drop.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\System32\spool\drivers\color\
  TargetFilename|endswith:
  - .dll
  - .exe
  - .sys
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/07/27/untangling-knotweed-european-private-sector-offensive-actor-using-0-day-exploits/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_spool_drivers_color_drop.yml)
