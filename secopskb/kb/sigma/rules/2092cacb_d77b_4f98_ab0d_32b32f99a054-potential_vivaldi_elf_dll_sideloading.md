---
sigma_id: "2092cacb-d77b-4f98-ab0d-32b32f99a054"
title: "Potential Vivaldi_elf.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_vivaldi_elf.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vivaldi_elf.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "2092cacb-d77b-4f98-ab0d-32b32f99a054"
  - "Potential Vivaldi_elf.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Vivaldi_elf.DLL Sideloading

Detects potential DLL sideloading of "vivaldi_elf.dll"

## Metadata

- Rule ID: 2092cacb-d77b-4f98-ab0d-32b32f99a054
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-08-03
- Source Path: rules/windows/image_load/image_load_side_load_vivaldi_elf.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \vivaldi_elf.dll
filter_main_legit_path:
  Image|endswith: \Vivaldi\Application\vivaldi.exe
  ImageLoaded|contains: \Vivaldi\Application\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vivaldi_elf.yml)
