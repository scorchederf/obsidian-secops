---
sigma_id: "41ca393d-538c-408a-ac27-cf1e038be80c"
title: "Directory Removal Via Rmdir"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_rmdir_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_rmdir_execution.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "41ca393d-538c-408a-ac27-cf1e038be80c"
  - "Directory Removal Via Rmdir"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Directory Removal Via Rmdir

Detects execution of the builtin "rmdir" command in order to delete directories.
Adversaries may delete files left behind by the actions of their intrusion activity.
Malware, tools, or other non-native files dropped or created on a system by an adversary may leave traces to indicate to what was done within a network and how.
Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

## Metadata

- Rule ID: 41ca393d-538c-408a-ac27-cf1e038be80c
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-15
- Modified: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_rmdir_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_rmdir:
  CommandLine|contains: rmdir
selection_flags:
  CommandLine|contains:
  - /s
  - /q
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.004/T1070.004.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/erase

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_rmdir_execution.yml)
