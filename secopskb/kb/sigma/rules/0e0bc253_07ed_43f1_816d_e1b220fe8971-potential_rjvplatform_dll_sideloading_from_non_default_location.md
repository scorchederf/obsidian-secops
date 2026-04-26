---
sigma_id: "0e0bc253-07ed-43f1-816d-e1b220fe8971"
title: "Potential RjvPlatform.DLL Sideloading From Non-Default Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_rjvplatform_non_default_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rjvplatform_non_default_location.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "0e0bc253-07ed-43f1-816d-e1b220fe8971"
  - "Potential RjvPlatform.DLL Sideloading From Non-Default Location"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential RjvPlatform.DLL Sideloading From Non-Default Location

Detects potential DLL sideloading of "RjvPlatform.dll" by "SystemResetPlatform.exe" located in a non-default location.

## Metadata

- Rule ID: 0e0bc253-07ed-43f1-816d-e1b220fe8971
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-09
- Source Path: rules/windows/image_load/image_load_side_load_rjvplatform_non_default_location.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \RjvPlatform.dll
  Image: \SystemResetPlatform.exe
filter_main_legit_path:
  Image|startswith: C:\Windows\System32\SystemResetPlatform\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://twitter.com/0gtweet/status/1666716511988330499

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rjvplatform_non_default_location.yml)
