---
sigma_id: "1fbc0671-5596-4e17-8682-f020a0b995dc"
title: "Potential CCleanerDU.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_ccleaner_du.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ccleaner_du.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "1fbc0671-5596-4e17-8682-f020a0b995dc"
  - "Potential CCleanerDU.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential CCleanerDU.DLL Sideloading

Detects potential DLL sideloading of "CCleanerDU.dll"

## Metadata

- Rule ID: 1fbc0671-5596-4e17-8682-f020a0b995dc
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-13
- Source Path: rules/windows/image_load/image_load_side_load_ccleaner_du.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \CCleanerDU.dll
filter_main_path:
  Image|startswith:
  - C:\Program Files\CCleaner\
  - C:\Program Files (x86)\CCleaner\
  Image|endswith:
  - \CCleaner.exe
  - \CCleaner64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives could occur from other custom installation paths. Apply additional filters accordingly.

## References

- https://lab52.io/blog/2344-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ccleaner_du.yml)
