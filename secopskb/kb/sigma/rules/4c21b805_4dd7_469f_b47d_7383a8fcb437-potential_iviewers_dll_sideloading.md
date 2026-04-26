---
sigma_id: "4c21b805-4dd7-469f-b47d-7383a8fcb437"
title: "Potential Iviewers.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_iviewers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_iviewers.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "4c21b805-4dd7-469f-b47d-7383a8fcb437"
  - "Potential Iviewers.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Iviewers.DLL Sideloading

Detects potential DLL sideloading of "iviewers.dll" (OLE/COM Object Interface Viewer)

## Metadata

- Rule ID: 4c21b805-4dd7-469f-b47d-7383a8fcb437
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-03-21
- Source Path: rules/windows/image_load/image_load_side_load_iviewers.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \iviewers.dll
filter:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Windows Kits\
  - C:\Program Files\Windows Kits\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.secureworks.com/research/shadowpad-malware-analysis

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_iviewers.yml)
