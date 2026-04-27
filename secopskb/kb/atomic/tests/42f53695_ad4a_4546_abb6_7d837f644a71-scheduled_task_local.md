---
atomic_guid: "42f53695-ad4a-4546-abb6-7d837f644a71"
title: "Scheduled task Local"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "42f53695-ad4a-4546-abb6-7d837f644a71"
  - "Scheduled task Local"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Upon successful execution, cmd.exe will create a scheduled task to spawn cmd.exe at 20:10.

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Input Arguments

### task_command

- description: What you want to execute
- type: string
- default: C:\windows\system32\cmd.exe

### time

- description: What time 24 Hour
- type: string
- default: 20:10

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
SCHTASKS /Create /SC ONCE /TN spawn /TR #{task_command} /ST #{time}
```

### Cleanup

```cmd
SCHTASKS /Delete /TN spawn /F >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
