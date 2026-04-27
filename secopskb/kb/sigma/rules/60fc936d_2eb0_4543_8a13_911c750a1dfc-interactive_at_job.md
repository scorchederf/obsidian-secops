---
sigma_id: "60fc936d-2eb0-4543-8a13-911c750a1dfc"
title: "Interactive AT Job"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "60fc936d-2eb0-4543-8a13-911c750a1dfc"
  - "Interactive AT Job"
attack_technique_ids:
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Interactive AT Job

Detects an interactive AT job, which may be used as a form of privilege escalation.

## Metadata

- Rule ID: 60fc936d-2eb0-4543-8a13-911c750a1dfc
- Status: test
- Level: high
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2019-10-24
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detection

```yaml
selection:
  Image|endswith: \at.exe
  CommandLine|contains: interactive
condition: selection
```

## False Positives

- Unlikely (at.exe deprecated as of Windows 8)

## Simulation

### At.exe Scheduled task

- Atomic Test: [[kb/atomic/tests/4a6c0dc4_0f2a_4203_9298_a5a9bdc21ed8-at_exe_scheduled_task|4a6c0dc4-0f2a-4203-9298-a5a9bdc21ed8]]
- atomic_guid: 4a6c0dc4-0f2a-4203-9298-a5a9bdc21ed8
- name: At.exe Scheduled task
- technique: T1053.002
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.002/T1053.002.md
- https://eqllib.readthedocs.io/en/latest/analytics/d8db43cf-ed52-4f5c-9fb3-c9a4b95a0b56.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml)
