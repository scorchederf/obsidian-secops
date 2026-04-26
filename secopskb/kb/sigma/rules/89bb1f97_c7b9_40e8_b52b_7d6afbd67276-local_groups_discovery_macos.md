---
sigma_id: "89bb1f97-c7b9-40e8-b52b-7d6afbd67276"
title: "Local Groups Discovery - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_local_groups.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_local_groups.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "89bb1f97-c7b9-40e8-b52b-7d6afbd67276"
  - "Local Groups Discovery - MacOs"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local Groups Discovery - MacOs

Detects enumeration of local system groups

## Metadata

- Rule ID: 89bb1f97-c7b9-40e8-b52b-7d6afbd67276
- Status: test
- Level: informational
- Author: Ömer Günal, Alejandro Ortuno, oscd.community
- Date: 2020-10-11
- Modified: 2022-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_local_groups.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_1:
  Image|endswith: /dscacheutil
  CommandLine|contains|all:
  - -q
  - group
selection_2:
  Image|endswith: /cat
  CommandLine|contains: /etc/group
selection_3:
  Image|endswith: /dscl
  CommandLine|contains|all:
  - -list
  - /groups
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.001/T1069.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_local_groups.yml)
