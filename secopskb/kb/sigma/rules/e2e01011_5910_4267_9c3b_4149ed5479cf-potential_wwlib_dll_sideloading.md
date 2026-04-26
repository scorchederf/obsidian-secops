---
sigma_id: "e2e01011-5910-4267-9c3b-4149ed5479cf"
title: "Potential WWlib.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_wwlib.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_wwlib.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "e2e01011-5910-4267-9c3b-4149ed5479cf"
  - "Potential WWlib.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential WWlib.DLL Sideloading

Detects potential DLL sideloading of "wwlib.dll"

## Metadata

- Rule ID: e2e01011-5910-4267-9c3b-4149ed5479cf
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-05-18
- Source Path: rules/windows/image_load/image_load_side_load_wwlib.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \wwlib.dll
filter_main_path:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft Office\
  - C:\Program Files\Microsoft Office\
  Image|endswith: \winword.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Microsoft Office\
  - C:\Program Files\Microsoft Office\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/WhichbufferArda/status/1658829954182774784
- https://news.sophos.com/en-us/2022/11/03/family-tree-dll-sideloading-cases-may-be-related/
- https://securelist.com/apt-luminousmoth/103332/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_wwlib.yml)
