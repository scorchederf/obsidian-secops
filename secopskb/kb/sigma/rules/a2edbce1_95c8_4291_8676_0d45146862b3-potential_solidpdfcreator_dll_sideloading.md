---
sigma_id: "a2edbce1-95c8-4291-8676-0d45146862b3"
title: "Potential SolidPDFCreator.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_solidpdfcreator.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_solidpdfcreator.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "a2edbce1-95c8-4291-8676-0d45146862b3"
  - "Potential SolidPDFCreator.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential SolidPDFCreator.DLL Sideloading

Detects potential DLL sideloading of "SolidPDFCreator.dll"

## Metadata

- Rule ID: a2edbce1-95c8-4291-8676-0d45146862b3
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-05-07
- Source Path: rules/windows/image_load/image_load_side_load_solidpdfcreator.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \SolidPDFCreator.dll
filter_main_path:
  Image|endswith: \SolidPDFCreator.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\SolidDocuments\SolidPDFCreator\
  - C:\Program Files\SolidDocuments\SolidPDFCreator\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_solidpdfcreator.yml)
