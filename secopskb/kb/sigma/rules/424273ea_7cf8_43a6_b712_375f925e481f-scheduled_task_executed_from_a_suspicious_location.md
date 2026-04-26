---
sigma_id: "424273ea-7cf8-43a6-b712-375f925e481f"
title: "Scheduled Task Executed From A Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/taskscheduler/win_taskscheduler_execution_from_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_execution_from_susp_locations.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / taskscheduler"
aliases:
  - "424273ea-7cf8-43a6-b712-375f925e481f"
  - "Scheduled Task Executed From A Suspicious Location"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Executed From A Suspicious Location

Detects the execution of Scheduled Tasks where the Program being run is located in a suspicious location or it's an unusale program to be run from a Scheduled Task

## Metadata

- Rule ID: 424273ea-7cf8-43a6-b712-375f925e481f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-05
- Modified: 2023-02-07
- Source Path: rules/windows/builtin/taskscheduler/win_taskscheduler_execution_from_susp_locations.yml

## Logsource

- definition: Requirements: The "Microsoft-Windows-TaskScheduler/Operational" is disabled by default and needs to be enabled in order for this detection to trigger
- product: windows
- service: taskscheduler

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection:
  EventID: 129
  Path|contains:
  - C:\Windows\Temp\
  - \AppData\Local\Temp\
  - \Desktop\
  - \Downloads\
  - \Users\Public\
  - C:\Temp\
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_execution_from_susp_locations.yml)
