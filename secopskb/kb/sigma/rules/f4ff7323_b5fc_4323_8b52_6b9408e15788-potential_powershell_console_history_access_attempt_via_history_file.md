---
sigma_id: "f4ff7323-b5fc-4323-8b52-6b9408e15788"
title: "Potential PowerShell Console History Access Attempt via History File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_console_history_file_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_console_history_file_access.yml"
build_date: "2026-04-26 14:14:32"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f4ff7323-b5fc-4323-8b52-6b9408e15788"
  - "Potential PowerShell Console History Access Attempt via History File"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PowerShell Console History Access Attempt via History File

Detects potential access attempts to the PowerShell console history directly via history file (ConsoleHost_history.txt).
This can give access to plaintext passwords used in PowerShell commands or used for general reconnaissance.

## Metadata

- Rule ID: f4ff7323-b5fc-4323-8b52-6b9408e15788
- Status: experimental
- Level: medium
- Author: Luc Génaux
- Date: 2025-04-03
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_console_history_file_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ConsoleHost_history.txt
  - (Get-PSReadLineOption).HistorySavePath
condition: selection
```

## False Positives

- Legitimate access of the console history file is possible

## References

- https://0xdf.gitlab.io/2018/11/08/powershell-history-file.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_console_history_file_access.yml)
