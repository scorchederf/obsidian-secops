---
sigma_id: "f8d6a15e-4bc8-4c27-8e5d-2b10f0b73e5b"
title: "Suspicious Powercfg Execution To Change Lock Screen Timeout"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powercfg_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powercfg_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f8d6a15e-4bc8-4c27-8e5d-2b10f0b73e5b"
  - "Suspicious Powercfg Execution To Change Lock Screen Timeout"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Powercfg Execution To Change Lock Screen Timeout

Detects suspicious execution of 'Powercfg.exe' to change lock screen timeout

## Metadata

- Rule ID: f8d6a15e-4bc8-4c27-8e5d-2b10f0b73e5b
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_powercfg_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_power:
- Image|endswith: \powercfg.exe
- OriginalFileName: PowerCfg.exe
selection_standby:
- CommandLine|contains|all:
  - '/setacvalueindex '
  - SCHEME_CURRENT
  - SUB_VIDEO
  - VIDEOCONLOCK
- CommandLine|contains|all:
  - '-change '
  - -standby-timeout-
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html
- https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powercfg_execution.yml)
