---
sigma_id: "d3feb4ee-ff1d-4d3d-bd10-5b28a238cc72"
title: "File and Directory Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_file_and_directory_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_file_and_directory_discovery.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "informational"
logsource: "linux / process_creation"
aliases:
  - "d3feb4ee-ff1d-4d3d-bd10-5b28a238cc72"
  - "File and Directory Discovery - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File and Directory Discovery - Linux

Detects usage of system utilities such as "find", "tree", "findmnt", etc, to discover files, directories and network shares.

## Metadata

- Rule ID: d3feb4ee-ff1d-4d3d-bd10-5b28a238cc72
- Status: test
- Level: informational
- Author: Daniil Yugoslavskiy, oscd.community, CheraghiMilad
- Date: 2020-10-19
- Modified: 2024-12-01
- Source Path: rules/linux/process_creation/proc_creation_lnx_file_and_directory_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection_file_with_asterisk:
  Image|endswith: /file
  CommandLine|re: (.){200,}
selection_recursive_ls:
  Image|endswith: /ls
  CommandLine|contains: -R
selection_find_execution:
  Image|endswith: /find
selection_tree_execution:
  Image|endswith: /tree
selection_findmnt_execution:
  Image|endswith: /findmnt
selection_locate_execution:
  Image|endswith: /mlocate
condition: 1 of selection_*
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1083/T1083.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_file_and_directory_discovery.yml)
