---
sigma_id: "8a7e90c5-fe6e-45dc-889e-057fe4378bd9"
title: "HackTool - SysmonEOP Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sysmoneop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sysmoneop.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "8a7e90c5-fe6e-45dc-889e-057fe4378bd9"
  - "HackTool - SysmonEOP Execution"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the PoC that can be used to exploit Sysmon CVE-2022-41120

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]

## Detection

```yaml
selection_img:
  Image|endswith: \SysmonEOP.exe
selection_hash:
  Hashes|contains:
  - IMPHASH=22F4089EB8ABA31E1BB162C6D9BF72E5
  - IMPHASH=5123FA4C4384D431CD0D893EEB49BBEC
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/Wh04m1001/SysmonEoP

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sysmoneop.yml)
