---
sigma_id: "88c0f9d8-30a8-4120-bb6b-ebb54abcf2a0"
title: "File Time Attribute Change"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_change_file_time_attr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_change_file_time_attr.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "88c0f9d8-30a8-4120-bb6b-ebb54abcf2a0"
  - "File Time Attribute Change"
attack_technique_ids:
  - "T1070.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Time Attribute Change

Detect file time attribute change to hide new or changes to existing files

## Metadata

- Rule ID: 88c0f9d8-30a8-4120-bb6b-ebb54abcf2a0
- Status: test
- Level: medium
- Author: Igor Fits, Mikhail Larin, oscd.community
- Date: 2020-10-19
- Modified: 2022-01-12
- Source Path: rules/macos/process_creation/proc_creation_macos_change_file_time_attr.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Detection

```yaml
selection:
  Image|endswith: /touch
  CommandLine|contains:
  - -t
  - -acmr
  - -d
  - -r
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.006/T1070.006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_change_file_time_attr.yml)
