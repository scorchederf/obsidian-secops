---
sigma_id: "3d48c9d3-1aa6-418d-98d3-8fd3c01a564e"
title: "Potential Mftrace.EXE Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mftrace_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mftrace_child_process.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3d48c9d3-1aa6-418d-98d3-8fd3c01a564e"
  - "Potential Mftrace.EXE Abuse"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Mftrace.EXE Abuse

Detects child processes of the "Trace log generation tool for Media Foundation Tools" (Mftrace.exe) which can abused to execute arbitrary binaries.

## Metadata

- Rule ID: 3d48c9d3-1aa6-418d-98d3-8fd3c01a564e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-09
- Modified: 2023-08-03
- Source Path: rules/windows/process_creation/proc_creation_win_mftrace_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
  ParentImage|endswith: \mftrace.exe
condition: selection
```

## False Positives

- Legitimate use for tracing purposes

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Mftrace/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mftrace_child_process.yml)
