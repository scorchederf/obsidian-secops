---
sigma_id: "f64c9b2d-b0ad-481d-9d03-7fc75020892a"
title: "Potential RoboForm.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_robform.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_robform.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "f64c9b2d-b0ad-481d-9d03-7fc75020892a"
  - "Potential RoboForm.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential RoboForm.DLL Sideloading

Detects potential DLL sideloading of "roboform.dll", a DLL used by RoboForm Password Manager

## Metadata

- Rule ID: f64c9b2d-b0ad-481d-9d03-7fc75020892a
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-14
- Source Path: rules/windows/image_load/image_load_side_load_robform.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \roboform.dll
  - \roboform-x64.dll
filter_main_path:
  Image|startswith:
  - ' C:\Program Files (x86)\Siber Systems\AI RoboForm\'
  - ' C:\Program Files\Siber Systems\AI RoboForm\'
  Image|endswith:
  - \robotaskbaricon.exe
  - \robotaskbaricon-x64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- If installed on a per-user level, the path would be located in "AppData\Local". Add additional filters to reflect this mode of installation

## References

- https://twitter.com/StopMalvertisin/status/1648604148848549888
- https://twitter.com/t3ft3lb/status/1656194831830401024
- https://www.roboform.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_robform.yml)
