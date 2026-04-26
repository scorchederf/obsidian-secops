---
sigma_id: "cc9d3712-6310-4320-b2df-7cb408274d53"
title: "Rebuild Performance Counter Values Via Lodctr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lodctr_performance_counter_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lodctr_performance_counter_tampering.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cc9d3712-6310-4320-b2df-7cb408274d53"
  - "Rebuild Performance Counter Values Via Lodctr.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rebuild Performance Counter Values Via Lodctr.EXE

Detects the execution of "lodctr.exe" to rebuild the performance counter registry values. This can be abused by attackers by providing a malicious config file to overwrite performance counter configuration to confuse and evade monitoring and security solutions.

## Metadata

- Rule ID: cc9d3712-6310-4320-b2df-7cb408274d53
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-15
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_lodctr_performance_counter_tampering.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \lodctr.exe
  OriginalFileName: LODCTR.EXE
selection_cli:
  CommandLine|contains|windash: ' -r'
condition: all of selection_*
```

## False Positives

- Legitimate usage by an administrator

## References

- https://learn.microsoft.com/en-us/windows/security/identity-protection/virtual-smart-cards/virtual-smart-card-tpmvscmgr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lodctr_performance_counter_tampering.yml)
