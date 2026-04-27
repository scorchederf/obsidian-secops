---
sigma_id: "2c32b543-1058-4808-91c6-5b31b8bed6c5"
title: "PUA - Crassus Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_crassus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_crassus.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2c32b543-1058-4808-91c6-5b31b8bed6c5"
  - "PUA - Crassus Execution"
attack_technique_ids:
  - "T1590.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Crassus, a Windows privilege escalation discovery tool, based on PE metadata characteristics.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1590-gather_victim_network_information#^t1590001-domain-properties|T1590.001: Domain Properties]]

## Detection

```yaml
selection:
- Image|endswith: \Crassus.exe
- OriginalFileName: Crassus.exe
- Description|contains: Crassus
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/vu-ls/Crassus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_crassus.yml)
