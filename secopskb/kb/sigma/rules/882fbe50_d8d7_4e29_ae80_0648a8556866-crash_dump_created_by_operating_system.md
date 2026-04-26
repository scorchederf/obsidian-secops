---
sigma_id: "882fbe50-d8d7-4e29-ae80-0648a8556866"
title: "Crash Dump Created By Operating System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_wer_systemerrorreporting/win_system_crash_dump_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_wer_systemerrorreporting/win_system_crash_dump_created.yml"
build_date: "2026-04-26 14:14:22"
status: "experimental"
level: "medium"
logsource: "windows / system"
aliases:
  - "882fbe50-d8d7-4e29-ae80-0648a8556866"
  - "Crash Dump Created By Operating System"
attack_technique_ids:
  - "T1003.002"
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Crash Dump Created By Operating System

Detects "BugCheck" errors indicating the system rebooted due to a crash, capturing the bugcheck code, dump file path, and report ID.

## Metadata

- Rule ID: 882fbe50-d8d7-4e29-ae80-0648a8556866
- Status: experimental
- Level: medium
- Author: Jason Mull
- Date: 2025-05-12
- Source Path: rules/windows/builtin/system/microsoft_windows_wer_systemerrorreporting/win_system_crash_dump_created.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection:
  Provider_Name: Microsoft-Windows-WER-SystemErrorReporting
  EventID: 1001
condition: selection
```

## References

- https://www.sans.edu/cyber-research/from-crash-compromise-unlocking-potential-windows-crash-dumps-offensive-security/
- https://jasonmull.com/articles/offensive/2025-05-12-windows-crash-dumps-offensive-security/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_wer_systemerrorreporting/win_system_crash_dump_created.yml)
