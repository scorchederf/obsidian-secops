---
sigma_id: "30aed7b6-d2c1-4eaf-9382-b6bc43e50c57"
title: "File Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_file_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_file_deletion.yml"
build_date: "2026-04-26 14:14:25"
status: "stable"
level: "informational"
logsource: "linux / process_creation"
aliases:
  - "30aed7b6-d2c1-4eaf-9382-b6bc43e50c57"
  - "File Deletion"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Deletion

Detects file deletion using "rm", "shred" or "unlink" commands which are used often by adversaries to delete files left behind by the actions of their intrusion activity

## Metadata

- Rule ID: 30aed7b6-d2c1-4eaf-9382-b6bc43e50c57
- Status: stable
- Level: informational
- Author: Ömer Günal, oscd.community
- Date: 2020-10-07
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_file_deletion.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  Image|endswith:
  - /rm
  - /shred
  - /unlink
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.004/T1070.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_file_deletion.yml)
