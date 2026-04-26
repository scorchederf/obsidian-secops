---
sigma_id: "d9047477-0359-48c9-b8c7-792cedcdc9c4"
title: "PUA - NirCmd Execution As LOCAL SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nircmd_as_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nircmd_as_system.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d9047477-0359-48c9-b8c7-792cedcdc9c4"
  - "PUA - NirCmd Execution As LOCAL SYSTEM"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - NirCmd Execution As LOCAL SYSTEM

Detects the use of NirCmd tool for command execution as SYSTEM user

## Metadata

- Rule ID: d9047477-0359-48c9-b8c7-792cedcdc9c4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-24
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_pua_nircmd_as_system.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection:
  CommandLine|contains: ' runassystem '
condition: selection
```

## False Positives

- Legitimate use by administrators

## References

- https://www.nirsoft.net/utils/nircmd.html
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/
- https://www.nirsoft.net/utils/nircmd2.html#using

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nircmd_as_system.yml)
