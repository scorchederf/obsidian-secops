---
sigma_id: "aaafa146-074c-11eb-adc1-0242ac120002"
title: "HackTool - Hydra Password Bruteforce Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_hydra.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hydra.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "aaafa146-074c-11eb-adc1-0242ac120002"
  - "HackTool - Hydra Password Bruteforce Execution"
attack_technique_ids:
  - "T1110"
  - "T1110.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects command line parameters used by Hydra password guessing hack tool

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110: Brute Force]]
- [[kb/attack/techniques/T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - '-u '
  - '-p '
  CommandLine|contains:
  - ^USER^
  - ^PASS^
condition: selection
```

## False Positives

- Software that uses the caret encased keywords PASS and USER in its command line

## References

- https://github.com/vanhauser-thc/thc-hydra

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hydra.yml)
