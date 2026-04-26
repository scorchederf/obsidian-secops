---
sigma_id: "ed825c86-c009-4014-b413-b76003e33d35"
title: "Windows Binary Executed From WSL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wsl_windows_binaries_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_windows_binaries_execution.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ed825c86-c009-4014-b413-b76003e33d35"
  - "Windows Binary Executed From WSL"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Binary Executed From WSL

Detects the execution of Windows binaries from within a WSL instance.
This could be used to masquerade parent-child relationships

## Metadata

- Rule ID: ed825c86-c009-4014-b413-b76003e33d35
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wsl_windows_binaries_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  Image|re: '[a-zA-Z]:\\'
  CurrentDirectory|contains: \\\\wsl.localhost
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_windows_binaries_execution.yml)
