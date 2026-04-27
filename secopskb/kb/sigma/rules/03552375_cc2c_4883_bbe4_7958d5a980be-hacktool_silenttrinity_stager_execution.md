---
sigma_id: "03552375-cc2c-4883-bbe4-7958d5a980be"
title: "HackTool - SILENTTRINITY Stager Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "03552375-cc2c-4883-bbe4-7958d5a980be"
  - "HackTool - SILENTTRINITY Stager Execution"
attack_technique_ids:
  - "T1071"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects SILENTTRINITY stager use via PE metadata

## Logsource

- category: process_creation
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml)
