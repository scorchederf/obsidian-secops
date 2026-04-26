---
sigma_id: "729ce0ea-5d8f-4769-9762-e35de441586d"
title: "MpiExec Lolbin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_mpiexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_mpiexec.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "729ce0ea-5d8f-4769-9762-e35de441586d"
  - "MpiExec Lolbin"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MpiExec Lolbin

Detects a certain command line flag combination used by mpiexec.exe LOLBIN from HPC pack that can be used to execute any other binary

## Metadata

- Rule ID: 729ce0ea-5d8f-4769-9762-e35de441586d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-11
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_mpiexec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_binary:
- Image|endswith: \mpiexec.exe
- Hashes|contains: IMPHASH=d8b52ef6aaa3a81501bdfff9dbb96217
selection_flags:
  CommandLine|contains:
  - ' /n 1 '
  - ' -n 1 '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1465058133303246867
- https://learn.microsoft.com/en-us/powershell/high-performance-computing/mpiexec?view=hpc19-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_mpiexec.yml)
