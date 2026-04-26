---
sigma_id: "13c02350-4177-4e45-ac17-cf7ca628ff5e"
title: "Files With System DLL Name In Unsuspected Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_creation_system_dll_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_system_dll_files.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "13c02350-4177-4e45-ac17-cf7ca628ff5e"
  - "Files With System DLL Name In Unsuspected Locations"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Files With System DLL Name In Unsuspected Locations

Detects the creation of a file with the ".dll" extension that has the name of a System DLL in uncommon or unsuspected locations. (Outisde of "System32", "SysWOW64", etc.).
It is highly recommended to perform an initial baseline before using this rule in production.

## Metadata

- Rule ID: 13c02350-4177-4e45-ac17-cf7ca628ff5e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-24
- Source Path: rules/windows/file/file_event/file_event_win_creation_system_dll_files.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \secur32.dll
  - \tdh.dll
filter_main_generic:
  TargetFilename|contains:
  - C:\$WINDOWS.~BT\
  - C:\$WinREAgent\
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
  - C:\Windows\uus\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Third party software might bundle specific versions of system DLLs.

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_system_dll_files.yml)
