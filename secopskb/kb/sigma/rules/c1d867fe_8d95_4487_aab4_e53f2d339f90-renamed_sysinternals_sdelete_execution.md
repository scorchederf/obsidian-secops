---
sigma_id: "c1d867fe-8d95-4487-aab4-e53f2d339f90"
title: "Renamed Sysinternals Sdelete Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_sysinternals_sdelete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_sdelete.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c1d867fe-8d95-4487-aab4-e53f2d339f90"
  - "Renamed Sysinternals Sdelete Execution"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed Sysinternals Sdelete Execution

Detects the use of a renamed SysInternals Sdelete, which is something an administrator shouldn't do (the renaming)

## Metadata

- Rule ID: c1d867fe-8d95-4487-aab4-e53f2d339f90
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-06
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_sysinternals_sdelete.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  OriginalFileName: sdelete.exe
filter:
  Image|endswith:
  - \sdelete.exe
  - \sdelete64.exe
condition: selection and not filter
```

## False Positives

- System administrator usage

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1485/T1485.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_sdelete.yml)
