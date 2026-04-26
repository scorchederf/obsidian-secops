---
sigma_id: "cf93e05e-d798-4d9e-b522-b0248dc61eaf"
title: "HackTool - SharpChisel Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cf93e05e-d798-4d9e-b522-b0248dc61eaf"
  - "HackTool - SharpChisel Execution"
attack_technique_ids:
  - "T1090.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - SharpChisel Execution

Detects usage of the Sharp Chisel via the commandline arguments

## Metadata

- Rule ID: cf93e05e-d798-4d9e-b522-b0248dc61eaf
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-05
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.001]]

## Detection

```yaml
selection:
- Image|endswith: \SharpChisel.exe
- Product: SharpChisel
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/shantanu561993/SharpChisel
- https://www.sentinelone.com/labs/wading-through-muddy-waters-recent-activity-of-an-iranian-state-sponsored-threat-actor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml)
