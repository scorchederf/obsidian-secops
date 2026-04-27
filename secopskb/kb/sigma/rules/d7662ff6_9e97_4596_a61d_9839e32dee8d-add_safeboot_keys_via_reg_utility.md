---
sigma_id: "d7662ff6-9e97-4596-a61d-9839e32dee8d"
title: "Add SafeBoot Keys Via Reg Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_add_safeboot.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_add_safeboot.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d7662ff6-9e97-4596-a61d-9839e32dee8d"
  - "Add SafeBoot Keys Via Reg Utility"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of "reg.exe" commands with the "add" or "copy" flags on safe boot registry keys. Often used by attacker to allow the ransomware to work in safe mode as some security products do not

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_safeboot:
  CommandLine|contains: \SYSTEM\CurrentControlSet\Control\SafeBoot
selection_flag:
  CommandLine|contains:
  - ' copy '
  - ' add '
condition: all of selection*
```

## False Positives

- Unlikely

## References

- https://redacted.com/blog/bianlian-ransomware-gang-gives-it-a-go/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_add_safeboot.yml)
