---
sigma_id: "ee218c12-627a-4d27-9e30-d6fb2fe22ed2"
title: "Powershell Inline Execution From A File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_exec_data_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_exec_data_file.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ee218c12-627a-4d27-9e30-d6fb2fe22ed2"
  - "Powershell Inline Execution From A File"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Inline Execution From A File

Detects inline execution of PowerShell code from a file

## Metadata

- Rule ID: ee218c12-627a-4d27-9e30-d6fb2fe22ed2
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_exec_data_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_exec:
  CommandLine|contains:
  - 'iex '
  - 'Invoke-Expression '
  - 'Invoke-Command '
  - 'icm '
selection_read:
  CommandLine|contains:
  - 'cat '
  - 'get-content '
  - 'type '
selection_raw:
  CommandLine|contains: ' -raw'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=50

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_exec_data_file.yml)
