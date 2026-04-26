---
sigma_id: "ff301988-c231-4bd0-834c-ac9d73b86586"
title: "PowerShell Console History Logs Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_powershell_command_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_powershell_command_history.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "ff301988-c231-4bd0-834c-ac9d73b86586"
  - "PowerShell Console History Logs Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Console History Logs Deleted

Detects the deletion of the PowerShell console History logs which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: ff301988-c231-4bd0-834c-ac9d73b86586
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_powershell_command_history.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  TargetFilename|endswith: \PSReadLine\ConsoleHost_history.txt
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_powershell_command_history.yml)
