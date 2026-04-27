---
sigma_id: "ff23ffbc-3378-435e-992f-0624dcf93ab4"
title: "HackTool - PurpleSharp Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_purplesharp_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_purplesharp_indicators.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "ff23ffbc-3378-435e-992f-0624dcf93ab4"
  - "HackTool - PurpleSharp Execution"
attack_technique_ids:
  - "T1587"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the PurpleSharp adversary simulation tool

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587: Develop Capabilities]]

## Detection

```yaml
selection_img:
- Image|contains: \purplesharp
- OriginalFileName: PurpleSharp.exe
selection_cli:
  CommandLine|contains:
  - xyz123456.exe
  - PurpleSharp
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/mvelazc0/PurpleSharp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_purplesharp_indicators.yml)
