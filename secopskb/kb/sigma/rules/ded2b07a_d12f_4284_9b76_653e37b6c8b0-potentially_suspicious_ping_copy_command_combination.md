---
sigma_id: "ded2b07a-d12f-4284-9b76-653e37b6c8b0"
title: "Potentially Suspicious Ping/Copy Command Combination"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_ping_copy_combined_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ping_copy_combined_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ded2b07a-d12f-4284-9b76-653e37b6c8b0"
  - "Potentially Suspicious Ping/Copy Command Combination"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Ping/Copy Command Combination

Detects uncommon and potentially suspicious one-liner command containing both "ping" and "copy" at the same time, which is usually used by malware.

## Metadata

- Rule ID: ded2b07a-d12f-4284-9b76-653e37b6c8b0
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-18
- Modified: 2024-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_ping_copy_combined_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection_cmd:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_action:
  CommandLine|contains|all:
  - ping
  - 'copy '
selection_cli_1:
  CommandLine|contains|windash: ' -n '
selection_cli_2:
  CommandLine|contains|windash: ' -y '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ping_copy_combined_execution.yml)
