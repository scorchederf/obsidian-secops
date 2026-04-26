---
sigma_id: "16fe46bb-4f64-46aa-817d-ff7bec4a2352"
title: "LiveKD Driver Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "16fe46bb-4f64-46aa-817d-ff7bec4a2352"
  - "LiveKD Driver Creation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LiveKD Driver Creation

Detects the creation of the LiveKD driver, which is used for live kernel debugging

## Metadata

- Rule ID: 16fe46bb-4f64-46aa-817d-ff7bec4a2352
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-16
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename: C:\Windows\System32\drivers\LiveKdD.SYS
  Image|endswith:
  - \livekd.exe
  - \livek64.exe
condition: selection
```

## False Positives

- Legitimate usage of LiveKD for debugging purposes will also trigger this

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver.yml)
