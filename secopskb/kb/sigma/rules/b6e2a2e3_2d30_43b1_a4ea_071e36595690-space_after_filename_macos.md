---
sigma_id: "b6e2a2e3-2d30-43b1-a4ea-071e36595690"
title: "Space After Filename - macOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_space_after_filename.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_space_after_filename.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "b6e2a2e3-2d30-43b1-a4ea-071e36595690"
  - "Space After Filename - macOS"
attack_technique_ids:
  - "T1036.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Space After Filename - macOS

Detects attempts to masquerade as legitimate files by adding a space to the end of the filename.

## Metadata

- Rule ID: b6e2a2e3-2d30-43b1-a4ea-071e36595690
- Status: test
- Level: low
- Author: remotephone
- Date: 2021-11-20
- Modified: 2023-01-04
- Source Path: rules/macos/process_creation/proc_creation_macos_space_after_filename.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.006]]

## Detection

```yaml
selection1:
  CommandLine|endswith: ' '
selection2:
  Image|endswith: ' '
condition: 1 of selection*
```

## False Positives

- Mistyped commands or legitimate binaries named to match the pattern

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1036.006/T1036.006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_space_after_filename.yml)
