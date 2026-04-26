---
sigma_id: "71158e3f-df67-472b-930e-7d287acaa3e1"
title: "Execution Of Non-Existing File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_image_missing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_image_missing.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "71158e3f-df67-472b-930e-7d287acaa3e1"
  - "Execution Of Non-Existing File"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execution Of Non-Existing File

Checks whether the image specified in a process creation event is not a full, absolute path (caused by process ghosting or other unorthodox methods to start a process)

## Metadata

- Rule ID: 71158e3f-df67-472b-930e-7d287acaa3e1
- Status: test
- Level: high
- Author: Max Altgelt (Nextron Systems)
- Date: 2021-12-09
- Modified: 2022-12-14
- Source Path: rules/windows/process_creation/proc_creation_win_susp_image_missing.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
image_absolute_path:
  Image|contains: \
filter_null:
  Image: null
filter_empty:
  Image:
  - '-'
  - ''
filter_4688:
- Image:
  - System
  - Registry
  - MemCompression
  - vmmem
- CommandLine:
  - Registry
  - MemCompression
  - vmmem
condition: not image_absolute_path and not 1 of filter*
```

## False Positives

- Unknown

## References

- https://pentestlaboratories.com/2021/12/08/process-ghosting/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_image_missing.yml)
