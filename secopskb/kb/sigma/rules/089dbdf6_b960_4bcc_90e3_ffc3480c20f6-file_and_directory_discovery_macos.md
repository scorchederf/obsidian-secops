---
sigma_id: "089dbdf6-b960-4bcc-90e3-ffc3480c20f6"
title: "File and Directory Discovery - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_file_and_directory_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_file_and_directory_discovery.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "089dbdf6-b960-4bcc-90e3-ffc3480c20f6"
  - "File and Directory Discovery - MacOS"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File and Directory Discovery - MacOS

Detects usage of system utilities to discover files and directories

## Metadata

- Rule ID: 089dbdf6-b960-4bcc-90e3-ffc3480c20f6
- Status: test
- Level: informational
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2022-11-25
- Source Path: rules/macos/process_creation/proc_creation_macos_file_and_directory_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
select_file_with_asterisk:
  Image: /usr/bin/file
  CommandLine|re: (.){200,}
select_recursive_ls:
  Image: /bin/ls
  CommandLine|contains: -R
select_find_execution:
  Image: /usr/bin/find
select_mdfind_execution:
  Image: /usr/bin/mdfind
select_tree_execution|endswith:
  Image: /tree
condition: 1 of select*
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1083/T1083.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_file_and_directory_discovery.yml)
