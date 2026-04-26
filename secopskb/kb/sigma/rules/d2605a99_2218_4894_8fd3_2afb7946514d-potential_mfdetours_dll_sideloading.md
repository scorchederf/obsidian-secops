---
sigma_id: "d2605a99-2218-4894-8fd3-2afb7946514d"
title: "Potential Mfdetours.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_mfdetours.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mfdetours.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "d2605a99-2218-4894-8fd3-2afb7946514d"
  - "Potential Mfdetours.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Mfdetours.DLL Sideloading

Detects potential DLL sideloading of "mfdetours.dll". While using "mftrace.exe" it can be abused to attach to an arbitrary process and force load any DLL named "mfdetours.dll" from the current directory of execution.

## Metadata

- Rule ID: d2605a99-2218-4894-8fd3-2afb7946514d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-03
- Source Path: rules/windows/image_load/image_load_side_load_mfdetours.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \mfdetours.dll
filter_main_legit_path:
  ImageLoaded|contains: :\Program Files (x86)\Windows Kits\10\bin\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mfdetours.yml)
