---
sigma_id: "d7c75059-2901-4578-b209-8837fd31c6a8"
title: "Proxy Execution via Vshadow"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vshadow_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d7c75059-2901-4578-b209-8837fd31c6a8"
  - "Proxy Execution via Vshadow"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Proxy Execution via Vshadow

Detects the invocation of vshadow.exe with the -exec parameter that executes a specified script or command after the shadow copies are created but before the VShadow tool exits.
VShadow is a command-line tool that you can use to create and manage volume shadow copies. While legitimate backup or administrative scripts may use this flag,
attackers can leverage this parameter to proxy the execution of malware.

## Metadata

- Rule ID: d7c75059-2901-4578-b209-8837fd31c6a8
- Status: experimental
- Level: medium
- Author: David Faiss
- Date: 2025-05-26
- Source Path: rules/windows/process_creation/proc_creation_win_vshadow_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith: \vshadow.exe
- OriginalFileName: vshadow.exe
selection_cli:
  CommandLine|contains: -exec
condition: all of selection_*
```

## False Positives

- System backup or administrator tools
- Legitimate administrative scripts

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Vshadow/
- https://learn.microsoft.com/en-us/windows/win32/vss/vshadow-tool-and-sample

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml)
