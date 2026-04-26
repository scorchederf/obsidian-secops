---
sigma_id: "952ed57c-8f99-453d-aee0-53a49c22f95d"
title: "Potential AVKkid.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_avkkid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_avkkid.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "952ed57c-8f99-453d-aee0-53a49c22f95d"
  - "Potential AVKkid.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential AVKkid.DLL Sideloading

Detects potential DLL sideloading of "AVKkid.dll"

## Metadata

- Rule ID: 952ed57c-8f99-453d-aee0-53a49c22f95d
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-08-03
- Source Path: rules/windows/image_load/image_load_side_load_avkkid.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \AVKkid.dll
filter_main_legit_path:
  Image|contains:
  - C:\Program Files (x86)\G DATA\
  - C:\Program Files\G DATA\
  Image|endswith: \AVKKid.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\G DATA\
  - C:\Program Files\G DATA\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_avkkid.yml)
