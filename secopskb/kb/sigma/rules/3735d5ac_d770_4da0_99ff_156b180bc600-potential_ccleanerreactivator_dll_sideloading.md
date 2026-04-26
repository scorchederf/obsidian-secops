---
sigma_id: "3735d5ac-d770-4da0-99ff-156b180bc600"
title: "Potential CCleanerReactivator.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_ccleaner_reactivator.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ccleaner_reactivator.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "3735d5ac-d770-4da0-99ff-156b180bc600"
  - "Potential CCleanerReactivator.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential CCleanerReactivator.DLL Sideloading

Detects potential DLL sideloading of "CCleanerReactivator.dll"

## Metadata

- Rule ID: 3735d5ac-d770-4da0-99ff-156b180bc600
- Status: test
- Level: medium
- Author: X__Junior
- Date: 2023-07-13
- Source Path: rules/windows/image_load/image_load_side_load_ccleaner_reactivator.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \CCleanerReactivator.dll
filter_main_path:
  Image|startswith:
  - C:\Program Files\CCleaner\
  - C:\Program Files (x86)\CCleaner\
  Image|endswith: \CCleanerReactivator.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives could occur from other custom installation paths. Apply additional filters accordingly.

## References

- https://lab52.io/blog/2344-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ccleaner_reactivator.yml)
