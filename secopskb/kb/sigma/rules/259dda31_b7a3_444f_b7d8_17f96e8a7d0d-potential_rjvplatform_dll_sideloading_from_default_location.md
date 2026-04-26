---
sigma_id: "259dda31-b7a3-444f-b7d8-17f96e8a7d0d"
title: "Potential RjvPlatform.DLL Sideloading From Default Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_rjvplatform_default_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rjvplatform_default_location.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "259dda31-b7a3-444f-b7d8-17f96e8a7d0d"
  - "Potential RjvPlatform.DLL Sideloading From Default Location"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential RjvPlatform.DLL Sideloading From Default Location

Detects loading of "RjvPlatform.dll" by the "SystemResetPlatform.exe" binary which can be abused as a method of DLL side loading since the "$SysReset" directory isn't created by default.

## Metadata

- Rule ID: 259dda31-b7a3-444f-b7d8-17f96e8a7d0d
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-09
- Source Path: rules/windows/image_load/image_load_side_load_rjvplatform_default_location.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image: C:\Windows\System32\SystemResetPlatform\SystemResetPlatform.exe
  ImageLoaded: C:\$SysReset\Framework\Stack\RjvPlatform.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1666716511988330499

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rjvplatform_default_location.yml)
