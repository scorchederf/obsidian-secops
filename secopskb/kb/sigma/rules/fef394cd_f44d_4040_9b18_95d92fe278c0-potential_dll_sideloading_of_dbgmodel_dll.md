---
sigma_id: "fef394cd-f44d-4040-9b18-95d92fe278c0"
title: "Potential DLL Sideloading Of DbgModel.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_dbgmodel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbgmodel.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "fef394cd-f44d-4040-9b18-95d92fe278c0"
  - "Potential DLL Sideloading Of DbgModel.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of DbgModel.DLL

Detects potential DLL sideloading of "DbgModel.dll"

## Metadata

- Rule ID: fef394cd-f44d-4040-9b18-95d92fe278c0
- Status: test
- Level: medium
- Author: Gary Lobermier
- Date: 2024-07-11
- Modified: 2024-07-22
- Source Path: rules/windows/image_load/image_load_side_load_dbgmodel.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \dbgmodel.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
filter_optional_windbg:
  ImageLoaded|startswith: C:\Program Files\WindowsApps\Microsoft.WinDbg_
filter_optional_windows_kits:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Windows Kits\
  - C:\Program Files\Windows Kits\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate applications loading their own versions of the DLL mentioned in this rule

## References

- https://hijacklibs.net/entries/microsoft/built-in/dbgmodel.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbgmodel.yml)
