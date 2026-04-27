---
sigma_id: "9e3cb244-bdb8-4632-8c90-6079c8f4f16d"
title: "Important Scheduled Task Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/taskscheduler/win_taskscheduler_susp_schtasks_delete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_susp_schtasks_delete.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / taskscheduler"
aliases:
  - "9e3cb244-bdb8-4632-8c90-6079c8f4f16d"
  - "Important Scheduled Task Deleted"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when adversaries try to stop system services or processes by deleting their respective scheduled tasks in order to conduct data destructive activities

## Logsource

- definition: Requirements: The "Microsoft-Windows-TaskScheduler/Operational" is disabled by default and needs to be enabled in order for this detection to trigger
- product: windows
- service: taskscheduler

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489: Service Stop]]

## Detection

```yaml
selection:
  EventID: 141
  TaskName|contains:
  - \Windows\SystemRestore\SR
  - \Windows\Windows Defender\
  - \Windows\BitLocker
  - \Windows\WindowsBackup\
  - \Windows\WindowsUpdate\
  - \Windows\UpdateOrchestrator\
  - \Windows\ExploitGuard
filter:
  UserName|contains:
  - AUTHORI
  - AUTORI
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/taskscheduler/win_taskscheduler_susp_schtasks_delete.yml)
