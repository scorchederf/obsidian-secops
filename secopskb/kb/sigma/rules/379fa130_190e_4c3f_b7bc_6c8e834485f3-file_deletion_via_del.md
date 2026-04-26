---
sigma_id: "379fa130-190e-4c3f-b7bc-6c8e834485f3"
title: "File Deletion Via Del"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_del_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_del_execution.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "379fa130-190e-4c3f-b7bc-6c8e834485f3"
  - "File Deletion Via Del"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Deletion Via Del

Detects execution of the builtin "del"/"erase" commands in order to delete files.
Adversaries may delete files left behind by the actions of their intrusion activity.
Malware, tools, or other non-native files dropped or created on a system by an adversary may leave traces to indicate to what was done within a network and how.
Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.

## Metadata

- Rule ID: 379fa130-190e-4c3f-b7bc-6c8e834485f3
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-15
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_del_execution.yml

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
selection_del:
  CommandLine|contains:
  - 'del '
  - 'erase '
selection_flags:
  CommandLine|contains|windash:
  - ' -f'
  - ' -s'
  - ' -q'
condition: all of selection_*
```

## False Positives

- False positives levels will differ Depending on the environment. You can use a combination of ParentImage and other keywords from the CommandLine field to filter legitimate activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.004/T1070.004.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/erase

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_del_execution.yml)
