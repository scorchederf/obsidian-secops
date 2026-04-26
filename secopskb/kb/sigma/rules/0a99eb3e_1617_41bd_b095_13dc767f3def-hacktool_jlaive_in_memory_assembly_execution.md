---
sigma_id: "0a99eb3e-1617-41bd-b095-13dc767f3def"
title: "HackTool - Jlaive In-Memory Assembly Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_jlaive_batch_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_jlaive_batch_execution.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0a99eb3e-1617-41bd-b095-13dc767f3def"
  - "HackTool - Jlaive In-Memory Assembly Execution"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Jlaive In-Memory Assembly Execution

Detects the use of Jlaive to execute assemblies in a copied PowerShell

## Metadata

- Rule ID: 0a99eb3e-1617-41bd-b095-13dc767f3def
- Status: test
- Level: medium
- Author: Jose Luis Sanchez Martinez (@Joseliyo_Jstnk)
- Date: 2022-05-24
- Modified: 2023-02-22
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_jlaive_batch_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
parent_selection:
  ParentImage|endswith: \cmd.exe
  ParentCommandLine|endswith: .bat
selection1:
  Image|endswith: \xcopy.exe
  CommandLine|contains|all:
  - powershell.exe
  - .bat.exe
selection2:
  Image|endswith: \xcopy.exe
  CommandLine|contains|all:
  - pwsh.exe
  - .bat.exe
selection3:
  Image|endswith: \attrib.exe
  CommandLine|contains|all:
  - +s
  - +h
  - .bat.exe
condition: parent_selection and (1 of selection*)
```

## False Positives

- Unknown

## References

- https://jstnk9.github.io/jstnk9/research/Jlaive-Antivirus-Evasion-Tool
- https://web.archive.org/web/20220514073704/https://github.com/ch2sh/Jlaive

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_jlaive_batch_execution.yml)
