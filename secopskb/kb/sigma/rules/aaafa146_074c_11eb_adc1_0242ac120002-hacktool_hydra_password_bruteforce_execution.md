---
sigma_id: "aaafa146-074c-11eb-adc1-0242ac120002"
title: "HackTool - Hydra Password Bruteforce Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_hydra.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hydra.yml"
build_date: "2026-04-26 17:03:19"
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

# HackTool - Hydra Password Bruteforce Execution

Detects command line parameters used by Hydra password guessing hack tool

## Metadata

- Rule ID: aaafa146-074c-11eb-adc1-0242ac120002
- Status: test
- Level: high
- Author: Vasiliy Burov
- Date: 2020-10-05
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_hydra.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

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
