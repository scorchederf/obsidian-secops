---
sigma_id: "d047726b-c71c-4048-a99b-2e2f50dc107d"
title: "Kavremover Dropped Binary LOLBIN Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_kavremover_uncommon_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kavremover_uncommon_execution.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d047726b-c71c-4048-a99b-2e2f50dc107d"
  - "Kavremover Dropped Binary LOLBIN Usage"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Kavremover Dropped Binary LOLBIN Usage

Detects the execution of a signed binary dropped by Kaspersky Lab Products Remover (kavremover) which can be abused as a LOLBIN to execute arbitrary commands and binaries.

## Metadata

- Rule ID: d047726b-c71c-4048-a99b-2e2f50dc107d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-01
- Source Path: rules/windows/process_creation/proc_creation_win_kavremover_uncommon_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
  CommandLine|contains: ' run run-cmd '
filter_main_legit_parents:
  ParentImage|endswith:
  - \cleanapi.exe
  - \kavremover.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://nasbench.medium.com/lolbined-using-kaspersky-endpoint-security-kes-installer-to-execute-arbitrary-commands-1c999f1b7fea

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_kavremover_uncommon_execution.yml)
