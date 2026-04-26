---
atomic_guid: "4a6c0dc4-0f2a-4203-9298-a5a9bdc21ed8"
title: "At.exe Scheduled task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.002"
attack_technique_name: "Scheduled Task/Job: At"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.002/T1053.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "4a6c0dc4-0f2a-4203-9298-a5a9bdc21ed8"
  - "At.exe Scheduled task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# At.exe Scheduled task

Executes cmd.exe
Note: deprecated in Windows 8+

Upon successful execution, cmd.exe will spawn at.exe and create a scheduled task that will spawn cmd at a specific time.

## Metadata

- Atomic GUID: 4a6c0dc4-0f2a-4203-9298-a5a9bdc21ed8
- Technique: T1053.002: Scheduled Task/Job: At
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1053.002/T1053.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
at 13:20 /interactive cmd
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.002/T1053.002.yaml)
