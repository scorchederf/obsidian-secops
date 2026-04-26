---
sigma_id: "7773b877-5abb-4a3e-b9c9-fd0369b59b00"
title: "WMIC Remote Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_remote_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_remote_execution.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7773b877-5abb-4a3e-b9c9-fd0369b59b00"
  - "WMIC Remote Command Execution"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMIC Remote Command Execution

Detects the execution of WMIC to query information on a remote system

## Metadata

- Rule ID: 7773b877-5abb-4a3e-b9c9-fd0369b59b00
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-14
- Modified: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_remote_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \WMIC.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|windash: '/node:'
filter_main_localhost:
  CommandLine|contains:
  - localhost
  - 127.0.0.1
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_remote_execution.yml)
