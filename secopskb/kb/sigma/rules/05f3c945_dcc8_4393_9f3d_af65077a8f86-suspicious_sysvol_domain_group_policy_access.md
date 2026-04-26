---
sigma_id: "05f3c945-dcc8-4393-9f3d-af65077a8f86"
title: "Suspicious SYSVOL Domain Group Policy Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_sysvol_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sysvol_access.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "05f3c945-dcc8-4393-9f3d-af65077a8f86"
  - "Suspicious SYSVOL Domain Group Policy Access"
attack_technique_ids:
  - "T1552.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious SYSVOL Domain Group Policy Access

Detects Access to Domain Group Policies stored in SYSVOL

## Metadata

- Rule ID: 05f3c945-dcc8-4393-9f3d-af65077a8f86
- Status: test
- Level: medium
- Author: Markus Neis, Jonhnathan Ribeiro, oscd.community
- Date: 2018-04-09
- Modified: 2022-01-07
- Source Path: rules/windows/process_creation/proc_creation_win_susp_sysvol_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.006]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \SYSVOL\
  - \policies\
condition: selection
```

## False Positives

- Administrative activity

## References

- https://adsecurity.org/?p=2288
- https://www.hybrid-analysis.com/sample/f2943f5e45befa52fb12748ca7171d30096e1d4fc3c365561497c618341299d5?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sysvol_access.yml)
