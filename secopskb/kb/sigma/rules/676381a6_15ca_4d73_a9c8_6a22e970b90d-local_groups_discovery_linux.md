---
sigma_id: "676381a6-15ca-4d73-a9c8-6a22e970b90d"
title: "Local Groups Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_local_groups.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_local_groups.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "676381a6-15ca-4d73-a9c8-6a22e970b90d"
  - "Local Groups Discovery - Linux"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local Groups Discovery - Linux

Detects enumeration of local system groups. Adversaries may attempt to find local system groups and permission settings

## Metadata

- Rule ID: 676381a6-15ca-4d73-a9c8-6a22e970b90d
- Status: test
- Level: low
- Author: Ömer Günal, Alejandro Ortuno, oscd.community
- Date: 2020-10-11
- Modified: 2025-06-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_local_groups.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_1:
  Image|endswith: /groups
selection_2:
  Image|endswith:
  - /cat
  - /ed
  - /head
  - /less
  - /more
  - /nano
  - /tail
  - /vi
  - /vim
  CommandLine|contains: /etc/group
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.001/T1069.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_local_groups.yml)
