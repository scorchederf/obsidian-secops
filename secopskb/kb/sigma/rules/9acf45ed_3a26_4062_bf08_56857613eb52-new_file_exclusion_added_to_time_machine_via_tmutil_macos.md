---
sigma_id: "9acf45ed-3a26-4062-bf08-56857613eb52"
title: "New File Exclusion Added To Time Machine Via Tmutil - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_tmutil_exclude_file_from_backup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_exclude_file_from_backup.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "9acf45ed-3a26-4062-bf08-56857613eb52"
  - "New File Exclusion Added To Time Machine Via Tmutil - MacOS"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New File Exclusion Added To Time Machine Via Tmutil - MacOS

Detects the addition of a new file or path exclusion to MacOS Time Machine via the "tmutil" utility.
An adversary could exclude a path from Time Machine backups to prevent certain files from being backed up.

## Metadata

- Rule ID: 9acf45ed-3a26-4062-bf08-56857613eb52
- Status: test
- Level: medium
- Author: Pratinav Chandra
- Date: 2024-05-29
- Source Path: rules/macos/process_creation/proc_creation_macos_tmutil_exclude_file_from_backup.yml

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
  CommandLine|contains: addexclusion
condition: all of selection_*
```

## False Positives

- Legitimate administrator activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.md#atomic-test-12---disable-time-machine
- https://www.loobins.io/binaries/tmutil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tmutil_exclude_file_from_backup.yml)
