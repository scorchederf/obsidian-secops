---
sigma_id: "5ba243e5-8165-4cf7-8c69-e1d3669654c1"
title: "Potential DLL Sideloading Of MpSvc.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_mpsvc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mpsvc.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "5ba243e5-8165-4cf7-8c69-e1d3669654c1"
  - "Potential DLL Sideloading Of MpSvc.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of MpSvc.DLL

Detects potential DLL sideloading of "MpSvc.dll".

## Metadata

- Rule ID: 5ba243e5-8165-4cf7-8c69-e1d3669654c1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema
- Date: 2024-07-11
- Source Path: rules/windows/image_load/image_load_side_load_mpsvc.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \MpSvc.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Program Files\Windows Defender\
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate applications loading their own versions of the DLL mentioned in this rule.

## References

- https://hijacklibs.net/entries/microsoft/built-in/mpsvc.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mpsvc.yml)
