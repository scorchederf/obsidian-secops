---
sigma_id: "576426ad-0131-4001-ae01-be175da0c108"
title: "PowerShell Script Dropped Via PowerShell.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_drop_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_drop_powershell.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "576426ad-0131-4001-ae01-be175da0c108"
  - "PowerShell Script Dropped Via PowerShell.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script Dropped Via PowerShell.EXE

Detects PowerShell creating a PowerShell file (.ps1). While often times this behavior is benign, sometimes it can be a sign of a dropper script trying to achieve persistence.

## Metadata

- Rule ID: 576426ad-0131-4001-ae01-be175da0c108
- Status: test
- Level: low
- Author: frack113
- Date: 2023-05-09
- Source Path: rules/windows/file/file_event/file_event_win_powershell_drop_powershell.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetFilename|endswith: .ps1
filter_main_psscriptpolicytest:
  TargetFilename|contains: __PSScriptPolicyTest_
filter_main_appdata:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains: \AppData\Local\Temp\
filter_main_windows_temp:
  TargetFilename|startswith: C:\Windows\Temp\
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives will differ depending on the environment and scripts used. Apply additional filters accordingly.

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_drop_powershell.yml)
