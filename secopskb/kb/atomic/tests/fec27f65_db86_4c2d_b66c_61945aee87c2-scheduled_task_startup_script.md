---
atomic_guid: "fec27f65-db86-4c2d-b66c-61945aee87c2"
title: "Scheduled Task Startup Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "fec27f65-db86-4c2d-b66c-61945aee87c2"
  - "Scheduled Task Startup Script"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scheduled Task Startup Script

Run an exe on user logon or system startup.  Upon execution, success messages will be displayed for the two scheduled tasks. To view
the tasks, open the Task Scheduler and look in the Active Tasks pane.

## Metadata

- Atomic GUID: fec27f65-db86-4c2d-b66c-61945aee87c2
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
schtasks /create /tn "T1053_005_OnLogon" /sc onlogon /tr "cmd.exe /c calc.exe"
schtasks /create /tn "T1053_005_OnStartup" /sc onstart /ru system /tr "cmd.exe /c calc.exe"
```

### Cleanup

```commandprompt
schtasks /delete /tn "T1053_005_OnLogon" /f >nul 2>&1
schtasks /delete /tn "T1053_005_OnStartup" /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
