---
sigma_id: "cdb15e19-c2d0-432a-928e-e49c8c60dcf2"
title: "Potential DLL Sideloading Of MsCorSvc.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_mscorsvc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mscorsvc.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "cdb15e19-c2d0-432a-928e-e49c8c60dcf2"
  - "Potential DLL Sideloading Of MsCorSvc.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of MsCorSvc.DLL

Detects potential DLL sideloading of "mscorsvc.dll".

## Metadata

- Rule ID: cdb15e19-c2d0-432a-928e-e49c8c60dcf2
- Status: test
- Level: medium
- Author: Wietze Beukema
- Date: 2024-07-11
- Modified: 2025-02-26
- Source Path: rules/windows/image_load/image_load_side_load_mscorsvc.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \mscorsvc.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Windows\Microsoft.NET\Framework\
  - C:\Windows\Microsoft.NET\Framework64\
  - C:\Windows\Microsoft.NET\FrameworkArm\
  - C:\Windows\Microsoft.NET\FrameworkArm64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate applications loading their own versions of the DLL mentioned in this rule.

## References

- https://hijacklibs.net/entries/microsoft/built-in/mscorsvc.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mscorsvc.yml)
