---
sigma_id: "3c05e90d-7eba-4324-9972-5d7f711a60a8"
title: "UAC Bypass Tools Using ComputerDefaults"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3c05e90d-7eba-4324-9972-5d7f711a60a8"
  - "UAC Bypass Tools Using ComputerDefaults"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Tools Using ComputerDefaults

Detects tools such as UACMe used to bypass UAC with computerdefaults.exe (UACMe 59)

## Metadata

- Rule ID: 3c05e90d-7eba-4324-9972-5d7f711a60a8
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-31
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
  Image: C:\Windows\System32\ComputerDefaults.exe
filter:
  ParentImage|contains:
  - :\Windows\System32
  - :\Program Files
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml)
