---
sigma_id: "75c505b1-711d-4f68-a357-8c3fe37dbf2d"
title: "HackTool - SILENTTRINITY Stager DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_hktl_silenttrinity_stager.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects SILENTTRINITY stager dll loading activity

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071: Application Layer Protocol]]

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
