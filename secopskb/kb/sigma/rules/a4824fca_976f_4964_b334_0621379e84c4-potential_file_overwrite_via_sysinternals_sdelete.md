---
sigma_id: "a4824fca-976f-4964-b334-0621379e84c4"
title: "Potential File Overwrite Via Sysinternals SDelete"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_sdelete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sdelete.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a4824fca-976f-4964-b334-0621379e84c4"
  - "Potential File Overwrite Via Sysinternals SDelete"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of SDelete to erase a file not the free space

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485: Data Destruction]]

## Detection

```yaml
selection:
  OriginalFileName: sdelete.exe
filter:
  CommandLine|contains:
  - ' -h'
  - ' -c'
  - ' -z'
  - ' /\?'
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1485/T1485.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sdelete.yml)
