---
sigma_id: "059c5af9-5131-4d8d-92b2-de4ad6146712"
title: "LiveKD Driver Creation By Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver_susp_creation.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "059c5af9-5131-4d8d-92b2-de4ad6146712"
  - "LiveKD Driver Creation By Uncommon Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LiveKD Driver Creation By Uncommon Process

Detects the creation of the LiveKD driver by a process image other than "livekd.exe".

## Metadata

- Rule ID: 059c5af9-5131-4d8d-92b2-de4ad6146712
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-16
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename: C:\Windows\System32\drivers\LiveKdD.SYS
filter_main_legit_name:
  Image|endswith:
  - \livekd.exe
  - \livek64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrators might rename LiveKD before its usage which could trigger this. Add additional names you use to the filter

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_livekd_driver_susp_creation.yml)
