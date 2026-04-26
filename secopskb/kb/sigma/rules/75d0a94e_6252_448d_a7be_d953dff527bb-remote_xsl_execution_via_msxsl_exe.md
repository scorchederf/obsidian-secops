---
sigma_id: "75d0a94e-6252-448d-a7be-d953dff527bb"
title: "Remote XSL Execution Via Msxsl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msxsl_remote_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msxsl_remote_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "75d0a94e-6252-448d-a7be-d953dff527bb"
  - "Remote XSL Execution Via Msxsl.EXE"
attack_technique_ids:
  - "T1220"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote XSL Execution Via Msxsl.EXE

Detects the execution of the "msxsl" binary with an "http" keyword in the command line. This might indicate a potential remote execution of XSL files.

## Metadata

- Rule ID: 75d0a94e-6252-448d-a7be-d953dff527bb
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_msxsl_remote_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

## Detection

```yaml
selection:
  Image|endswith: \msxsl.exe
  CommandLine|contains: http
condition: selection
```

## False Positives

- Msxsl is not installed by default and is deprecated, so unlikely on most systems.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1220/T1220.md
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Msxsl/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msxsl_remote_execution.yml)
