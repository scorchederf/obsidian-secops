---
sigma_id: "4f6edb78-5c21-42ab-a558-fd2a6fc1fd57"
title: "Potential 7za.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_7za.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_7za.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "low"
logsource: "windows / image_load"
aliases:
  - "4f6edb78-5c21-42ab-a558-fd2a6fc1fd57"
  - "Potential 7za.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential 7za.DLL Sideloading

Detects potential DLL sideloading of "7za.dll"

## Metadata

- Rule ID: 4f6edb78-5c21-42ab-a558-fd2a6fc1fd57
- Status: test
- Level: low
- Author: X__Junior
- Date: 2023-06-09
- Source Path: rules/windows/image_load/image_load_side_load_7za.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \7za.dll
filter_main_legit_path:
  Image|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  ImageLoaded|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate third party application located in "AppData" may leverage this DLL to offer 7z compression functionality and may generate false positives. Apply additional filters as needed.

## References

- https://www.gov.pl/attachment/ee91f24d-3e67-436d-aa50-7fa56acf789d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_7za.yml)
