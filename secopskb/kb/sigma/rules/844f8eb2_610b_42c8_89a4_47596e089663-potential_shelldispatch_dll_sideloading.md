---
sigma_id: "844f8eb2-610b-42c8-89a4-47596e089663"
title: "Potential ShellDispatch.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_shelldispatch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_shelldispatch.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "844f8eb2-610b-42c8-89a4-47596e089663"
  - "Potential ShellDispatch.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential ShellDispatch.DLL Sideloading

Detects potential DLL sideloading of "ShellDispatch.dll"

## Metadata

- Rule ID: 844f8eb2-610b-42c8-89a4-47596e089663
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-20
- Source Path: rules/windows/image_load/image_load_side_load_shelldispatch.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \ShellDispatch.dll
filter_main_legit_path:
- ImageLoaded|contains|all:
  - :\Users\
  - \AppData\Local\Temp\
- ImageLoaded|contains: :\Windows\Temp\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Some installers may trigger some false positives

## References

- https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_shelldispatch.yml)
