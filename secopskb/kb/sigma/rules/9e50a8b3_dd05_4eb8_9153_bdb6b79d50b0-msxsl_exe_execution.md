---
sigma_id: "9e50a8b3-dd05-4eb8-9153-bdb6b79d50b0"
title: "Msxsl.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msxsl_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msxsl_execution.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9e50a8b3-dd05-4eb8-9153-bdb6b79d50b0"
  - "Msxsl.EXE Execution"
attack_technique_ids:
  - "T1220"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Msxsl.EXE Execution

Detects the execution of the MSXSL utility. This can be used to execute Extensible Stylesheet Language (XSL) files. These files are commonly used to describe the processing and rendering of data within XML files.
Adversaries can abuse this functionality to execute arbitrary files while potentially bypassing application whitelisting defenses.

## Metadata

- Rule ID: 9e50a8b3-dd05-4eb8-9153-bdb6b79d50b0
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_msxsl_execution.yml

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
condition: selection
```

## False Positives

- Msxsl is not installed by default and is deprecated, so unlikely on most systems.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1220/T1220.md
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Msxsl/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msxsl_execution.yml)
