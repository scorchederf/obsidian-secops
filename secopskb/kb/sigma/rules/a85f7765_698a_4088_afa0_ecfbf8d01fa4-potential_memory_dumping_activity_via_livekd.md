---
sigma_id: "a85f7765-698a-4088-afa0-ecfbf8d01fa4"
title: "Potential Memory Dumping Activity Via LiveKD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_livekd_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_livekd_execution.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a85f7765-698a-4088-afa0-ecfbf8d01fa4"
  - "Potential Memory Dumping Activity Via LiveKD"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Memory Dumping Activity Via LiveKD

Detects execution of LiveKD based on PE metadata or image name

## Metadata

- Rule ID: a85f7765-698a-4088-afa0-ecfbf8d01fa4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-15
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_livekd_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith:
  - \livekd.exe
  - \livekd64.exe
- OriginalFileName: livekd.exe
condition: selection
```

## False Positives

- Administration and debugging activity (must be investigated)

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/livekd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_livekd_execution.yml)
