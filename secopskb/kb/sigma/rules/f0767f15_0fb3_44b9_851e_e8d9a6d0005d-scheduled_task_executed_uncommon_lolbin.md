---
sigma_id: "f0767f15-0fb3-44b9-851e-e8d9a6d0005d"
title: "Scheduled Task Executed Uncommon LOLBIN"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/taskscheduler/win_taskscheduler_lolbin_execution_via_task_scheduler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_lolbin_execution_via_task_scheduler.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / taskscheduler"
aliases:
  - "f0767f15-0fb3-44b9-851e-e8d9a6d0005d"
  - "Scheduled Task Executed Uncommon LOLBIN"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Executed Uncommon LOLBIN

Detects the execution of Scheduled Tasks where the program being run is located in a suspicious location or where it is an unusual program to be run from a Scheduled Task

## Metadata

- Rule ID: f0767f15-0fb3-44b9-851e-e8d9a6d0005d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-05
- Modified: 2023-02-07
- Source Path: rules/windows/builtin/taskscheduler/win_taskscheduler_lolbin_execution_via_task_scheduler.yml

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
  Path|endswith:
  - \calc.exe
  - \cscript.exe
  - \mshta.exe
  - \mspaint.exe
  - \notepad.exe
  - \regsvr32.exe
  - \wscript.exe
condition: selection
```

## False Positives

- False positives may occur with some of the selected binaries if you have tasks using them (which could be very common in your environment). Exclude all the specific trusted tasks before using this rule

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_lolbin_execution_via_task_scheduler.yml)
