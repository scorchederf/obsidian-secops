---
sigma_id: "37e8d358-6408-4853-82f4-98333fca7014"
title: "Remote Access Tool - NetSupport Execution From Unusual Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_netsupport_susp_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_netsupport_susp_exec.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "37e8d358-6408-4853-82f4-98333fca7014"
  - "Remote Access Tool - NetSupport Execution From Unusual Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - NetSupport Execution From Unusual Location

Detects execution of client32.exe (NetSupport RAT) from an unusual location (outside of 'C:\Program Files')

## Metadata

- Rule ID: 37e8d358-6408-4853-82f4-98333fca7014
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-19
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_netsupport_susp_exec.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith: \client32.exe
- Product|contains: NetSupport Remote Control
- OriginalFileName|contains: client32.exe
- Hashes|contains: IMPHASH=a9d50692e95b79723f3e76fcf70d023e
filter:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_netsupport_susp_exec.yml)
