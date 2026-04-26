---
sigma_id: "3d3aa6cd-6272-44d6-8afc-7e88dfef7061"
title: "Change Default File Association Via Assoc"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_assoc_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_assoc_execution.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "3d3aa6cd-6272-44d6-8afc-7e88dfef7061"
  - "Change Default File Association Via Assoc"
attack_technique_ids:
  - "T1546.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Change Default File Association Via Assoc

Detects file association changes using the builtin "assoc" command.
When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Metadata

- Rule ID: 3d3aa6cd-6272-44d6-8afc-7e88dfef7061
- Status: test
- Level: low
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_assoc_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains: assoc
condition: all of selection_*
```

## False Positives

- Admin activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.001/T1546.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_assoc_execution.yml)
