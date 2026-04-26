---
sigma_id: "cd8c163e-a19b-402e-bdd5-419ff5859f12"
title: "HackTool - ADCSPwn Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_adcspwn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_adcspwn.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cd8c163e-a19b-402e-bdd5-419ff5859f12"
  - "HackTool - ADCSPwn Execution"
attack_technique_ids:
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - ADCSPwn Execution

Detects command line parameters used by ADCSPwn, a tool to escalate privileges in an active directory network by coercing authenticate from machine accounts and relaying to the certificate service

## Metadata

- Rule ID: cd8c163e-a19b-402e-bdd5-419ff5859f12
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-31
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_adcspwn.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ' --adcs '
  - ' --port '
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/bats3c/ADCSPwn

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_adcspwn.yml)
