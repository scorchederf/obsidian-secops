---
sigma_id: "7c9340a9-e2ee-4e43-94c5-c54ebbea1006"
title: "File And SubFolder Enumeration Via Dir Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_dir_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_dir_execution.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "7c9340a9-e2ee-4e43-94c5-c54ebbea1006"
  - "File And SubFolder Enumeration Via Dir Command"
attack_technique_ids:
  - "T1217"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File And SubFolder Enumeration Via Dir Command

Detects usage of the "dir" command part of Windows CMD with the "/S" command line flag in order to enumerate files in a specified directory and all subdirectories.

## Metadata

- Rule ID: 7c9340a9-e2ee-4e43-94c5-c54ebbea1006
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-13
- Modified: 2024-04-14
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_dir_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Detection

```yaml
selection_cmd:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains|windash: dir*-s
condition: all of selection_*
```

## False Positives

- Likely

## Simulation

### List Internet Explorer Bookmarks using the command prompt

- atomic_guid: 727dbcdb-e495-4ab1-a6c4-80c7f77aef85
- name: List Internet Explorer Bookmarks using the command prompt
- technique: T1217
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1217.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_dir_execution.yml)
