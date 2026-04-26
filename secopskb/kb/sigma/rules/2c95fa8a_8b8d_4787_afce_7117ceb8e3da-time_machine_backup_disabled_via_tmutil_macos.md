---
sigma_id: "2c95fa8a-8b8d-4787-afce-7117ceb8e3da"
title: "Time Machine Backup Disabled Via Tmutil - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_tmutil_disable_backup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_disable_backup.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "2c95fa8a-8b8d-4787-afce-7117ceb8e3da"
  - "Time Machine Backup Disabled Via Tmutil - MacOS"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Time Machine Backup Disabled Via Tmutil - MacOS

Detects disabling of Time Machine (Apple's automated backup utility software) via the native macOS backup utility "tmutil".
An attacker can use this to prevent backups from occurring.

## Metadata

- Rule ID: 2c95fa8a-8b8d-4787-afce-7117ceb8e3da
- Status: test
- Level: medium
- Author: Pratinav Chandra
- Date: 2024-05-29
- Source Path: rules/macos/process_creation/proc_creation_macos_tmutil_disable_backup.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection_img:
- Image|endswith: /tmutil
- CommandLine|contains: tmutil
selection_cmd:
  CommandLine|contains: disable
condition: all of selection_*
```

## False Positives

- Legitimate administrator activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.md#atomic-test-12---disable-time-machine
- https://www.loobins.io/binaries/tmutil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_disable_backup.yml)
