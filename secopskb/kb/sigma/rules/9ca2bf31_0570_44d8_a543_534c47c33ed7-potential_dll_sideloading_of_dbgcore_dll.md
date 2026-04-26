---
sigma_id: "9ca2bf31-0570-44d8-a543-534c47c33ed7"
title: "Potential DLL Sideloading Of DBGCORE.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_dbgcore.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbgcore.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "9ca2bf31-0570-44d8-a543-534c47c33ed7"
  - "Potential DLL Sideloading Of DBGCORE.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of DBGCORE.DLL

Detects DLL sideloading of "dbgcore.dll"

## Metadata

- Rule ID: 9ca2bf31-0570-44d8-a543-534c47c33ed7
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-10-25
- Modified: 2025-10-06
- Source Path: rules/windows/image_load/image_load_side_load_dbgcore.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \dbgcore.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SystemTemp\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
filter_optional_steam:
  ImageLoaded|endswith: \Steam\bin\cef\cef.win7x64\dbgcore.dll
filter_optional_opera:
  ImageLoaded|contains: opera\Opera Installer Temp\opera_package
  ImageLoaded|endswith: \assistant\dbgcore.dll
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate applications loading their own versions of the DLL mentioned in this rule

## References

- https://hijacklibs.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbgcore.yml)
