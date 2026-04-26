---
sigma_id: "75c505b1-711d-4f68-a357-8c3fe37dbf2d"
title: "HackTool - SILENTTRINITY Stager DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "75c505b1-711d-4f68-a357-8c3fe37dbf2d"
  - "HackTool - SILENTTRINITY Stager DLL Load"
attack_technique_ids:
  - "T1071"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SILENTTRINITY Stager DLL Load

Detects SILENTTRINITY stager dll loading activity

## Metadata

- Rule ID: 75c505b1-711d-4f68-a357-8c3fe37dbf2d
- Status: test
- Level: high
- Author: Aleksey Potapov, oscd.community
- Date: 2019-10-22
- Modified: 2023-02-17
- Source Path: rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071]]

## Detection

```yaml
selection:
  Description|contains: st2stager
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/byt3bl33d3r/SILENTTRINITY

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml)
