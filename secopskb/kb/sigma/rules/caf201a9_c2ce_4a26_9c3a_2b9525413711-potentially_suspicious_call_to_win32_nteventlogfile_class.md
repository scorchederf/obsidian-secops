---
sigma_id: "caf201a9-c2ce-4a26-9c3a-2b9525413711"
title: "Potentially Suspicious Call To Win32_NTEventlogFile Class"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_nteventlogfile_usage.yml"
build_date: "2026-04-27 19:13:54"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the WMI class "Win32_NTEventlogFile" in a potentially suspicious way (delete, backup, change permissions, etc.) from a PowerShell script

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
