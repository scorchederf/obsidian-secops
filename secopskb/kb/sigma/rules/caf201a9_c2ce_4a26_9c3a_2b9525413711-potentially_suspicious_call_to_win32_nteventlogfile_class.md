---
sigma_id: "caf201a9-c2ce-4a26-9c3a-2b9525413711"
title: "Potentially Suspicious Call To Win32_NTEventlogFile Class"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "caf201a9-c2ce-4a26-9c3a-2b9525413711"
  - "Potentially Suspicious Call To Win32_NTEventlogFile Class"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potentially Suspicious Call To Win32_NTEventlogFile Class

Detects usage of the WMI class "Win32_NTEventlogFile" in a potentially suspicious way (delete, backup, change permissions, etc.) from a PowerShell script

## Metadata

- Rule ID: caf201a9-c2ce-4a26-9c3a-2b9525413711
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-13
- Source Path: rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_class:
  CommandLine|contains: Win32_NTEventlogFile
selection_function:
  CommandLine|contains:
  - .BackupEventlog(
  - .ChangeSecurityPermissions(
  - .ChangeSecurityPermissionsEx(
  - .ClearEventLog(
  - .Delete(
  - .DeleteEx(
  - .Rename(
  - .TakeOwnerShip(
  - .TakeOwnerShipEx(
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml)
