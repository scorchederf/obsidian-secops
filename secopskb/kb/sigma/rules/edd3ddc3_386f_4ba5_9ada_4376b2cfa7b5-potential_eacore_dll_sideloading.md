---
sigma_id: "edd3ddc3-386f-4ba5-9ada-4376b2cfa7b5"
title: "Potential EACore.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_eacore.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_eacore.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "edd3ddc3-386f-4ba5-9ada-4376b2cfa7b5"
  - "Potential EACore.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential EACore.DLL Sideloading

Detects potential DLL sideloading of "EACore.dll"

## Metadata

- Rule ID: edd3ddc3-386f-4ba5-9ada-4376b2cfa7b5
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-08-03
- Source Path: rules/windows/image_load/image_load_side_load_eacore.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \EACore.dll
filter_main_legit_path:
  Image|contains|all:
  - C:\Program Files\Electronic Arts\EA Desktop\
  - \EACoreServer.exe
  ImageLoaded|startswith: C:\Program Files\Electronic Arts\EA Desktop\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_eacore.yml)
