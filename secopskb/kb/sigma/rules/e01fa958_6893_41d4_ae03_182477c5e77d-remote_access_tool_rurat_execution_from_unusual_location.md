---
sigma_id: "e01fa958-6893-41d4-ae03-182477c5e77d"
title: "Remote Access Tool - RURAT Execution From Unusual Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_rurat_non_default_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_rurat_non_default_location.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e01fa958-6893-41d4-ae03-182477c5e77d"
  - "Remote Access Tool - RURAT Execution From Unusual Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - RURAT Execution From Unusual Location

Detects execution of Remote Utilities RAT (RURAT) from an unusual location (outside of 'C:\Program Files')

## Metadata

- Rule ID: e01fa958-6893-41d4-ae03-182477c5e77d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-19
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_rurat_non_default_location.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith:
  - \rutserv.exe
  - \rfusclient.exe
- Product: Remote Utilities
filter:
  Image|startswith:
  - C:\Program Files\Remote Utilities
  - C:\Program Files (x86)\Remote Utilities
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_rurat_non_default_location.yml)
