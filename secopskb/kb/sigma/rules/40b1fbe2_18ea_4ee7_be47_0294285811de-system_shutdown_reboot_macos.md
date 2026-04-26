---
sigma_id: "40b1fbe2-18ea-4ee7-be47-0294285811de"
title: "System Shutdown/Reboot - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_system_shutdown_reboot.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_shutdown_reboot.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "40b1fbe2-18ea-4ee7-be47-0294285811de"
  - "System Shutdown/Reboot - MacOs"
attack_technique_ids:
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Shutdown/Reboot - MacOs

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems.

## Metadata

- Rule ID: 40b1fbe2-18ea-4ee7-be47-0294285811de
- Status: test
- Level: informational
- Author: Igor Fits, Mikhail Larin, oscd.community
- Date: 2020-10-19
- Modified: 2022-11-26
- Source Path: rules/macos/process_creation/proc_creation_macos_system_shutdown_reboot.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Detection

```yaml
selection:
  Image|endswith:
  - /shutdown
  - /reboot
  - /halt
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1529/T1529.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_shutdown_reboot.yml)
