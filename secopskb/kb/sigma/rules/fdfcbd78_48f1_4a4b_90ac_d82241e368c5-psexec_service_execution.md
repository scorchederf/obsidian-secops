---
sigma_id: "fdfcbd78-48f1-4a4b-90ac-d82241e368c5"
title: "PsExec Service Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fdfcbd78-48f1-4a4b-90ac-d82241e368c5"
  - "PsExec Service Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PsExec Service Execution

Detects launch of the PSEXESVC service, which means that this system was the target of a psexec remote execution

## Metadata

- Rule ID: fdfcbd78-48f1-4a4b-90ac-d82241e368c5
- Status: test
- Level: medium
- Author: Thomas Patzke, Romaissa Adjailia, Florian Roth (Nextron Systems)
- Date: 2017-06-12
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image: C:\Windows\PSEXESVC.exe
- OriginalFileName: psexesvc.exe
condition: selection
```

## False Positives

- Legitimate administrative tasks

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
- https://www.youtube.com/watch?v=ro2QuZTIMBM

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexesvc.yml)
