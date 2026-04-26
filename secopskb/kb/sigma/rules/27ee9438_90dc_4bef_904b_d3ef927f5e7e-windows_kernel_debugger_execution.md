---
sigma_id: "27ee9438-90dc-4bef-904b-d3ef927f5e7e"
title: "Windows Kernel Debugger Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_kd_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kd_execution.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "27ee9438-90dc-4bef-904b-d3ef927f5e7e"
  - "Windows Kernel Debugger Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Kernel Debugger Execution

Detects execution of the Windows Kernel Debugger "kd.exe".

## Metadata

- Rule ID: 27ee9438-90dc-4bef-904b-d3ef927f5e7e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-15
- Modified: 2024-04-24
- Source Path: rules/windows/process_creation/proc_creation_win_kd_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith: \kd.exe
- OriginalFileName: kd.exe
condition: selection
```

## False Positives

- Rare occasions of legitimate cases where kernel debugging is necessary in production. Investigation is required

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kd_execution.yml)
