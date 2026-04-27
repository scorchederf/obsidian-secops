---
sigma_id: "cf93e05e-d798-4d9e-b522-b0248dc61eaf"
title: "HackTool - SharpChisel Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_chisel.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the Sharp Chisel via the commandline arguments

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]

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
