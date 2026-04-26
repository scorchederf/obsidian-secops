---
sigma_id: "edadb1e5-5919-4e4c-8462-a9e643b02c4b"
title: "Process Memory Dump via RdrLeakDiag.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "edadb1e5-5919-4e4c-8462-a9e643b02c4b"
  - "Process Memory Dump via RdrLeakDiag.EXE"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Memory Dump via RdrLeakDiag.EXE

Detects the use of the Microsoft Windows Resource Leak Diagnostic tool "rdrleakdiag.exe" to dump process memory

## Metadata

- Rule ID: edadb1e5-5919-4e4c-8462-a9e643b02c4b
- Status: test
- Level: high
- Author: Cedric MAURUGEON, Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-09-24
- Modified: 2024-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \rdrleakdiag.exe
- OriginalFileName: RdrLeakDiag.exe
selection_cli_dump:
  CommandLine|contains|windash:
  - /memdmp
  - fullmemdmp
selection_cli_output_process:
  CommandLine|contains|windash:
  - ' /o '
  - ' /p '
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.pureid.io/dumping-abusing-windows-credentials-part-1/
- https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/
- https://lolbas-project.github.io/lolbas/Binaries/Rdrleakdiag/
- https://twitter.com/0gtweet/status/1299071304805560321?s=21
- https://news.sophos.com/en-us/2024/06/05/operation-crimson-palace-a-technical-deep-dive

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rdrleakdiag_process_dumping.yml)
