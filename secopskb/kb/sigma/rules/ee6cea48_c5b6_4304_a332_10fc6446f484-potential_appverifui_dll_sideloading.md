---
sigma_id: "ee6cea48-c5b6-4304-a332-10fc6446f484"
title: "Potential appverifUI.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_appverifui.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_appverifui.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "ee6cea48-c5b6-4304-a332-10fc6446f484"
  - "Potential appverifUI.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential appverifUI.DLL Sideloading

Detects potential DLL sideloading of "appverifUI.dll"

## Metadata

- Rule ID: ee6cea48-c5b6-4304-a332-10fc6446f484
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-20
- Source Path: rules/windows/image_load/image_load_side_load_appverifui.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \appverifUI.dll
filter_main_legit_path:
  Image:
  - C:\Windows\SysWOW64\appverif.exe
  - C:\Windows\System32\appverif.exe
  ImageLoaded|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://web.archive.org/web/20220519091349/https://fatrodzianko.com/2020/02/15/dll-side-loading-appverif-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_appverifui.yml)
