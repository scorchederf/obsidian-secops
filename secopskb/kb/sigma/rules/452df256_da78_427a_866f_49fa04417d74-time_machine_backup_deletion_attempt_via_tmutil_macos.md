---
sigma_id: "452df256-da78-427a-866f-49fa04417d74"
title: "Time Machine Backup Deletion Attempt Via Tmutil - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_tmutil_delete_backup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_delete_backup.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "452df256-da78-427a-866f-49fa04417d74"
  - "Time Machine Backup Deletion Attempt Via Tmutil - MacOS"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Time Machine Backup Deletion Attempt Via Tmutil - MacOS

Detects deletion attempts of MacOS Time Machine backups via the native backup utility "tmutil".
An adversary may perform this action before launching a ransonware attack to prevent the victim from restoring their files.

## Metadata

- Rule ID: 452df256-da78-427a-866f-49fa04417d74
- Status: test
- Level: medium
- Author: Pratinav Chandra
- Date: 2024-05-29
- Source Path: rules/macos/process_creation/proc_creation_macos_tmutil_delete_backup.yml

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
  CommandLine|contains: delete
condition: all of selection_*
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.md#atomic-test-12---disable-time-machine
- https://www.loobins.io/binaries/tmutil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_delete_backup.yml)
