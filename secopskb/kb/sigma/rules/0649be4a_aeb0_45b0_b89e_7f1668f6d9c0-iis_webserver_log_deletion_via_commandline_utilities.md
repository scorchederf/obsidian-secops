---
sigma_id: "0649be4a-aeb0-45b0-b89e-7f1668f6d9c0"
title: "IIS WebServer Log Deletion via CommandLine Utilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_logs_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_logs_deletion.yml"
build_date: "2026-04-26 14:14:27"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0649be4a-aeb0-45b0-b89e-7f1668f6d9c0"
  - "IIS WebServer Log Deletion via CommandLine Utilities"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# IIS WebServer Log Deletion via CommandLine Utilities

Detects attempts to delete Internet Information Services (IIS) log files via command line utilities, which is a common defense evasion technique used by attackers to cover their tracks.
Threat actors often abuse vulnerabilities in web applications hosted on IIS servers to gain initial access and later delete IIS logs to evade detection.

## Metadata

- Rule ID: 0649be4a-aeb0-45b0-b89e-7f1668f6d9c0
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-09-02
- Source Path: rules/windows/process_creation/proc_creation_win_iis_logs_deletion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \cmd.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - cmd.exe
  - powershell.exe
  - powershell_ise.exe
  - pwsh.dll
selection_cli_del:
  CommandLine|contains:
  - 'del '
  - 'erase '
  - 'rm '
  - 'remove-item '
  - 'rmdir '
selection_cli_iis_dir:
  CommandLine|contains: \inetpub\logs\
condition: all of selection_*
```

## False Positives

- Deletion of IIS logs that are older than a certain retention period as part of regular maintenance activities.
- Legitimate schedule tasks or scripts that clean up log files regularly.

## References

- https://learn.microsoft.com/en-us/iis/manage/provisioning-and-managing-iis/managing-iis-log-file-storage

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_logs_deletion.yml)
