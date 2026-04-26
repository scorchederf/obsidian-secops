---
sigma_id: "e4903324-1a10-4ed3-981b-f6fe3be3a2c2"
title: "Potential Edputil.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_edputil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_edputil.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "e4903324-1a10-4ed3-981b-f6fe3be3a2c2"
  - "Potential Edputil.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Edputil.DLL Sideloading

Detects potential DLL sideloading of "edputil.dll"

## Metadata

- Rule ID: e4903324-1a10-4ed3-981b-f6fe3be3a2c2
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-09
- Source Path: rules/windows/image_load/image_load_side_load_edputil.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \edputil.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://alternativeto.net/news/2023/5/cybercriminals-use-wordpad-vulnerability-to-spread-qbot-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_edputil.yml)
