---
sigma_id: "508a9374-ad52-4789-b568-fc358def2c65"
title: "Suspicious History File Operations"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_histfile_operations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_histfile_operations.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "508a9374-ad52-4789-b568-fc358def2c65"
  - "Suspicious History File Operations"
attack_technique_ids:
  - "T1552.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious History File Operations

Detects commandline operations on shell history files

## Metadata

- Rule ID: 508a9374-ad52-4789-b568-fc358def2c65
- Status: test
- Level: medium
- Author: Mikhail Larin, oscd.community
- Date: 2020-10-17
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_histfile_operations.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.003]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - .bash_history
  - .zsh_history
  - .zhistory
  - .history
  - .sh_history
  - fish_history
condition: selection
```

## False Positives

- Legitimate administrative activity
- Legitimate software, cleaning hist file

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.003/T1552.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_histfile_operations.yml)
