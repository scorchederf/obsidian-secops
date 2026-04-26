---
sigma_id: "d2d642d7-b393-43fe-bae4-e81ed5915c4b"
title: "Scheduled Task/Job At"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_at_command.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_at_command.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "d2d642d7-b393-43fe-bae4-e81ed5915c4b"
  - "Scheduled Task/Job At"
attack_technique_ids:
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task/Job At

Detects the use of at/atd which are utilities that are used to schedule tasks.
They are often abused by adversaries to maintain persistence or to perform task scheduling for initial or recurring execution of malicious code

## Metadata

- Rule ID: d2d642d7-b393-43fe-bae4-e81ed5915c4b
- Status: stable
- Level: low
- Author: Ömer Günal, oscd.community
- Date: 2020-10-06
- Modified: 2022-07-07
- Source Path: rules/linux/process_creation/proc_creation_lnx_at_command.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detection

```yaml
selection:
  Image|endswith:
  - /at
  - /atd
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.002/T1053.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_at_command.yml)
