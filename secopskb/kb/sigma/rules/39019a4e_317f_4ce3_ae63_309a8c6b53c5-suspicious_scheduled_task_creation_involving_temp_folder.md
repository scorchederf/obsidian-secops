---
sigma_id: "39019a4e-317f-4ce3-ae63-309a8c6b53c5"
title: "Suspicious Scheduled Task Creation Involving Temp Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation_temp_folder.yml"
build_date: "2026-04-27 19:13:57"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of scheduled tasks that involves a temporary folder and runs only once

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

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
