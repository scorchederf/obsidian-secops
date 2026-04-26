---
sigma_id: "9fbf5927-5261-4284-a71d-f681029ea574"
title: "Compress Data and Lock With Password for Exfiltration With 7-ZIP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_7zip_password_compression.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_7zip_password_compression.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9fbf5927-5261-4284-a71d-f681029ea574"
  - "Compress Data and Lock With Password for Exfiltration With 7-ZIP"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Compress Data and Lock With Password for Exfiltration With 7-ZIP

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party utilities

## Metadata

- Rule ID: 9fbf5927-5261-4284-a71d-f681029ea574
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-27
- Modified: 2023-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_7zip_password_compression.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_img:
- Description|contains: 7-Zip
- Image|endswith:
  - \7z.exe
  - \7zr.exe
  - \7za.exe
- OriginalFileName:
  - 7z.exe
  - 7za.exe
selection_password:
  CommandLine|contains: ' -p'
selection_action:
  CommandLine|contains:
  - ' a '
  - ' u '
condition: all of selection_*
```

## False Positives

- Legitimate activity is expected since compressing files with a password is common.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_7zip_password_compression.yml)
