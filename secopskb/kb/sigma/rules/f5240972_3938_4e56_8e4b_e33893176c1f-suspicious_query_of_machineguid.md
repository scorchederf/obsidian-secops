---
sigma_id: "f5240972-3938-4e56-8e4b-e33893176c1f"
title: "Suspicious Query of MachineGUID"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_machineguid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_machineguid.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "f5240972-3938-4e56-8e4b-e33893176c1f"
  - "Suspicious Query of MachineGUID"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Query of MachineGUID

Use of reg to get MachineGuid information

## Metadata

- Rule ID: f5240972-3938-4e56-8e4b-e33893176c1f
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-01
- Source Path: rules/windows/process_creation/proc_creation_win_reg_machineguid.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - SOFTWARE\Microsoft\Cryptography
  - '/v '
  - MachineGuid
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1082/T1082.md#atomic-test-8---windows-machineguid-discovery

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_machineguid.yml)
