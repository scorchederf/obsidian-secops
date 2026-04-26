---
sigma_id: "acf61bd8-d814-4272-81f0-a7a269aa69aa"
title: "Indicator Removal on Host - Clear Mac System Logs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_clear_system_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_clear_system_logs.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "acf61bd8-d814-4272-81f0-a7a269aa69aa"
  - "Indicator Removal on Host - Clear Mac System Logs"
attack_technique_ids:
  - "T1070.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Indicator Removal on Host - Clear Mac System Logs

Detects deletion of local audit logs

## Metadata

- Rule ID: acf61bd8-d814-4272-81f0-a7a269aa69aa
- Status: test
- Level: medium
- Author: remotephone, oscd.community
- Date: 2020-10-11
- Modified: 2022-09-16
- Source Path: rules/macos/process_creation/proc_creation_macos_clear_system_logs.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Detection

```yaml
selection1:
  Image|endswith:
  - /rm
  - /unlink
  - /shred
selection_cli_1:
  CommandLine|contains: /var/log
selection_cli_2:
  CommandLine|contains|all:
  - /Users/
  - /Library/Logs/
condition: selection1 and 1 of selection_cli*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.002/T1070.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_clear_system_logs.yml)
