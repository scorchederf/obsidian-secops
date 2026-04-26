---
sigma_id: "7f2bb9d5-6395-4de5-969c-70c11fbe6b12"
title: "Split A File Into Pieces"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_split_file_into_pieces.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_split_file_into_pieces.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "7f2bb9d5-6395-4de5-969c-70c11fbe6b12"
  - "Split A File Into Pieces"
attack_technique_ids:
  - "T1030"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Split A File Into Pieces

Detection use of the command "split" to split files into parts and possible transfer.

## Metadata

- Rule ID: 7f2bb9d5-6395-4de5-969c-70c11fbe6b12
- Status: test
- Level: low
- Author: Igor Fits, Mikhail Larin, oscd.community
- Date: 2020-10-15
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_split_file_into_pieces.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1030-data_transfer_size_limits|T1030]]

## Detection

```yaml
selection:
  Image|endswith: /split
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1030/T1030.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_split_file_into_pieces.yml)
