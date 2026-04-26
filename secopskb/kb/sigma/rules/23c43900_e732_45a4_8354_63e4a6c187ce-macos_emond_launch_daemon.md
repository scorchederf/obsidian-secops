---
sigma_id: "23c43900-e732-45a4-8354-63e4a6c187ce"
title: "MacOS Emond Launch Daemon"
framework: "sigma"
generated: "true"
source_path: "rules/macos/file_event/file_event_macos_emond_launch_daemon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/file_event/file_event_macos_emond_launch_daemon.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "macos / file_event"
aliases:
  - "23c43900-e732-45a4-8354-63e4a6c187ce"
  - "MacOS Emond Launch Daemon"
attack_technique_ids:
  - "T1546.014"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MacOS Emond Launch Daemon

Detects additions to the Emond Launch Daemon that adversaries may use to gain persistence and elevate privileges.

## Metadata

- Rule ID: 23c43900-e732-45a4-8354-63e4a6c187ce
- Status: test
- Level: medium
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-23
- Modified: 2021-11-27
- Source Path: rules/macos/file_event/file_event_macos_emond_launch_daemon.yml

## Logsource

- category: file_event
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.014]]

## Detection

```yaml
selection_1:
  TargetFilename|contains: /etc/emond.d/rules/
  TargetFilename|endswith: .plist
selection_2:
  TargetFilename|contains: /private/var/db/emondClients/
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.014/T1546.014.md
- https://posts.specterops.io/leveraging-emond-on-macos-for-persistence-a040a2785124

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/file_event/file_event_macos_emond_launch_daemon.yml)
