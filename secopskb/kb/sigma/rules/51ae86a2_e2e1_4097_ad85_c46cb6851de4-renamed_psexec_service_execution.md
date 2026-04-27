---
sigma_id: "51ae86a2-e2e1-4097-ad85-c46cb6851de4"
title: "Renamed PsExec Service Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_sysinternals_psexec_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_psexec_service.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "51ae86a2-e2e1-4097-ad85-c46cb6851de4"
  - "Renamed PsExec Service Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious launch of a renamed version of the PSEXESVC service with, which is not often used by legitimate administrators

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  OriginalFileName: psexesvc.exe
filter:
  Image: C:\Windows\PSEXESVC.exe
condition: selection and not filter
```

## False Positives

- Legitimate administrative tasks

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
- https://www.youtube.com/watch?v=ro2QuZTIMBM

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_psexec_service.yml)
