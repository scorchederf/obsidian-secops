---
sigma_id: "3d2a2d59-929c-4b78-8c1a-145dfe9e07b1"
title: "Publisher Attachment File Dropped In Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_publisher_files_in_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_publisher_files_in_susp_locations.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "3d2a2d59-929c-4b78-8c1a-145dfe9e07b1"
  - "Publisher Attachment File Dropped In Suspicious Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Publisher Attachment File Dropped In Suspicious Location

Detects creation of files with the ".pub" extension in suspicious or uncommon locations. This could be a sign of attackers abusing Publisher documents

## Metadata

- Rule ID: 3d2a2d59-929c-4b78-8c1a-145dfe9e07b1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-08
- Source Path: rules/windows/file/file_event/file_event_win_office_publisher_files_in_susp_locations.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|contains:
  - \AppData\Local\Temp\
  - \Users\Public\
  - \Windows\Temp\
  - C:\Temp\
  TargetFilename|endswith: .pub
condition: selection
```

## False Positives

- Legitimate usage of ".pub" files from those locations

## References

- https://twitter.com/EmericNasi/status/1623224526220804098

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_publisher_files_in_susp_locations.yml)
