---
sigma_id: "1182f3b3-e716-4efa-99ab-d2685d04360f"
title: "History File Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_history_delete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_history_delete.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "1182f3b3-e716-4efa-99ab-d2685d04360f"
  - "History File Deletion"
attack_technique_ids:
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# History File Deletion

Detects events in which a history file gets deleted, e.g. the ~/bash_history to remove traces of malicious activity

## Metadata

- Rule ID: 1182f3b3-e716-4efa-99ab-d2685d04360f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-20
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_history_delete.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation|T1565.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - /rm
  - /unlink
  - /shred
selection_history:
- CommandLine|contains:
  - /.bash_history
  - /.zsh_history
- CommandLine|endswith:
  - _history
  - .history
  - zhistory
condition: all of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/sleventyeleven/linuxprivchecker/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.003/T1552.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_history_delete.yml)
