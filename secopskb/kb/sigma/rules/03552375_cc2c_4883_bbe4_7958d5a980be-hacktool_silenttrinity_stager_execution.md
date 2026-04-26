---
sigma_id: "03552375-cc2c-4883-bbe4-7958d5a980be"
title: "HackTool - SILENTTRINITY Stager Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml"
build_date: "2026-04-26 14:14:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - SILENTTRINITY Stager Execution

Detects SILENTTRINITY stager use via PE metadata

## Metadata

- Rule ID: 03552375-cc2c-4883-bbe4-7958d5a980be
- Status: test
- Level: high
- Author: Aleksey Potapov, oscd.community
- Date: 2019-10-22
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml

## Logsource

- category: process_creation
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_silenttrinity_stager.yml)
