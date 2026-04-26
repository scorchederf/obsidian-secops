---
sigma_id: "9ef27c24-4903-4192-881a-3adde7ff92a5"
title: "Renamed Remote Utilities RAT (RURAT) Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_rurat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_rurat.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9ef27c24-4903-4192-881a-3adde7ff92a5"
  - "Renamed Remote Utilities RAT (RURAT) Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed Remote Utilities RAT (RURAT) Execution

Detects execution of renamed Remote Utilities (RURAT) via Product PE header field

## Metadata

- Rule ID: 9ef27c24-4903-4192-881a-3adde7ff92a5
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-19
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_rurat.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Software Tags

- S0592

## Detection

```yaml
selection:
  Product: Remote Utilities
filter:
  Image|endswith:
  - \rutserv.exe
  - \rfusclient.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_rurat.yml)
