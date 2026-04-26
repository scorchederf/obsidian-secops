---
sigma_id: "caa02837-f659-466f-bca6-48bde2826ab4"
title: "Potential DLL Sideloading Via ClassicExplorer32.dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_classicexplorer32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_classicexplorer32.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "caa02837-f659-466f-bca6-48bde2826ab4"
  - "Potential DLL Sideloading Via ClassicExplorer32.dll"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Via ClassicExplorer32.dll

Detects potential DLL sideloading using ClassicExplorer32.dll from the Classic Shell software

## Metadata

- Rule ID: caa02837-f659-466f-bca6-48bde2826ab4
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-13
- Source Path: rules/windows/image_load/image_load_side_load_classicexplorer32.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_classicexplorer:
  ImageLoaded|endswith: \ClassicExplorer32.dll
filter_classicexplorer:
  ImageLoaded|startswith: C:\Program Files\Classic Shell\
condition: selection_classicexplorer and not filter_classicexplorer
```

## False Positives

- Unknown

## References

- https://blogs.blackberry.com/en/2022/12/mustang-panda-uses-the-russian-ukrainian-war-to-attack-europe-and-asia-pacific-targets
- https://app.any.run/tasks/6d8cabb0-dcda-44b6-8050-28d6ce281687/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_classicexplorer32.yml)
