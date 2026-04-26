---
sigma_id: "e2e80da2-8c66-4e00-ae3c-2eebd29f6b6d"
title: "Compress Data and Lock With Password for Exfiltration With WINZIP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winzip_password_compression.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winzip_password_compression.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e2e80da2-8c66-4e00-ae3c-2eebd29f6b6d"
  - "Compress Data and Lock With Password for Exfiltration With WINZIP"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Compress Data and Lock With Password for Exfiltration With WINZIP

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party utilities

## Metadata

- Rule ID: e2e80da2-8c66-4e00-ae3c-2eebd29f6b6d
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-27
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_winzip_password_compression.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_winzip:
  CommandLine|contains:
  - winzip.exe
  - winzip64.exe
selection_password:
  CommandLine|contains: -s"
selection_other:
  CommandLine|contains:
  - ' -min '
  - ' -a '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winzip_password_compression.yml)
