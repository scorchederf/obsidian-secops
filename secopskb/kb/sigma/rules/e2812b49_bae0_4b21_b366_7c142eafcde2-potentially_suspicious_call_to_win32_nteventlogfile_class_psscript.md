---
sigma_id: "e2812b49-bae0-4b21-b366-7c142eafcde2"
title: "Potentially Suspicious Call To Win32_NTEventlogFile Class - PSScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_win32_nteventlogfile_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win32_nteventlogfile_usage.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "e2812b49-bae0-4b21-b366-7c142eafcde2"
  - "Potentially Suspicious Call To Win32_NTEventlogFile Class - PSScript"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Call To Win32_NTEventlogFile Class - PSScript

Detects usage of the WMI class "Win32_NTEventlogFile" in a potentially suspicious way (delete, backup, change permissions, etc.) from a PowerShell script

## Metadata

- Rule ID: e2812b49-bae0-4b21-b366-7c142eafcde2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-13
- Source Path: rules/windows/powershell/powershell_script/posh_ps_win32_nteventlogfile_usage.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## Detection

```yaml
selection_class:
  ScriptBlockText|contains: Win32_NTEventlogFile
selection_function:
  ScriptBlockText|contains:
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

- Legitimate administration and backup scripts

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win32_nteventlogfile_usage.yml)
