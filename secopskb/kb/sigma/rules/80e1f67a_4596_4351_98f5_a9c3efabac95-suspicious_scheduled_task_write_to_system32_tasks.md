---
sigma_id: "80e1f67a-4596-4351-98f5-a9c3efabac95"
title: "Suspicious Scheduled Task Write to System32 Tasks"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_task_write.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_task_write.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "80e1f67a-4596-4351-98f5-a9c3efabac95"
  - "Suspicious Scheduled Task Write to System32 Tasks"
attack_technique_ids:
  - "T1053"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of tasks from processes executed from suspicious locations

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

## Detection

```yaml
selection:
  TargetFilename|contains: \Windows\System32\Tasks
  Image|contains:
  - \AppData\
  - C:\PerfLogs
  - \Windows\System32\config\systemprofile
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_task_write.yml)
