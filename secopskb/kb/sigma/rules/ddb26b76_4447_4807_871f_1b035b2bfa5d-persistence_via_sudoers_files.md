---
sigma_id: "ddb26b76-4447-4807-871f-1b035b2bfa5d"
title: "Persistence Via Sudoers Files"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_persistence_sudoers_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_persistence_sudoers_files.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "linux / file_event"
aliases:
  - "ddb26b76-4447-4807-871f-1b035b2bfa5d"
  - "Persistence Via Sudoers Files"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via Sudoers Files

Detects creation of sudoers file or files in "sudoers.d" directory which can be used a potential method to persiste privileges for a specific user.

## Metadata

- Rule ID: ddb26b76-4447-4807-871f-1b035b2bfa5d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-05
- Modified: 2022-12-31
- Source Path: rules/linux/file_event/file_event_lnx_persistence_sudoers_files.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
selection:
  TargetFilename|startswith: /etc/sudoers.d/
condition: selection
```

## False Positives

- Creation of legitimate files in sudoers.d folder part of administrator work

## References

- https://github.com/h3xduck/TripleCross/blob/1f1c3e0958af8ad9f6ebe10ab442e75de33e91de/apps/deployer.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_persistence_sudoers_files.yml)
