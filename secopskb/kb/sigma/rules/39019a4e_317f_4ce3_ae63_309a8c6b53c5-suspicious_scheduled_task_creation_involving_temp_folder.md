---
sigma_id: "39019a4e-317f-4ce3-ae63-309a8c6b53c5"
title: "Suspicious Scheduled Task Creation Involving Temp Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "39019a4e-317f-4ce3-ae63-309a8c6b53c5"
  - "Suspicious Scheduled Task Creation Involving Temp Folder"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Scheduled Task Creation Involving Temp Folder

Detects the creation of scheduled tasks that involves a temporary folder and runs only once

## Metadata

- Rule ID: 39019a4e-317f-4ce3-ae63-309a8c6b53c5
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-03-11
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection:
  Image|endswith: \schtasks.exe
  CommandLine|contains|all:
  - ' /create '
  - ' /sc once '
  - \Temp\
condition: selection
```

## False Positives

- Administrative activity
- Software installation

## References

- https://discuss.elastic.co/t/detection-and-response-for-hafnium-activity/266289/3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml)
