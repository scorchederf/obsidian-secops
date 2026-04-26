---
sigma_id: "cd219ff3-fa99-45d4-8380-a7d15116c6dc"
title: "New User Created Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_user_add.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_add.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cd219ff3-fa99-45d4-8380-a7d15116c6dc"
  - "New User Created Via Net.EXE"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New User Created Via Net.EXE

Identifies the creation of local users via the net.exe command.

## Metadata

- Rule ID: cd219ff3-fa99-45d4-8380-a7d15116c6dc
- Status: test
- Level: medium
- Author: Endgame, JHasenbusch (adapted to Sigma for oscd.community)
- Date: 2018-10-30
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_user_add.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains|all:
  - user
  - add
condition: all of selection_*
```

## False Positives

- Legitimate user creation.
- Better use event IDs for user creation rather than command line rules.

## References

- https://eqllib.readthedocs.io/en/latest/analytics/014c3f51-89c6-40f1-ac9c-5688f26090ab.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.001/T1136.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_add.yml)
