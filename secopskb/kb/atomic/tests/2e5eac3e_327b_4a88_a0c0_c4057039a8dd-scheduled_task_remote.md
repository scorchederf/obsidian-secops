---
atomic_guid: "2e5eac3e-327b-4a88-a0c0-c4057039a8dd"
title: "Scheduled task Remote"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "2e5eac3e-327b-4a88-a0c0-c4057039a8dd"
  - "Scheduled task Remote"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scheduled task Remote

Create a task on a remote system.
Upon successful execution, cmd.exe will create a scheduled task to spawn cmd.exe at 20:10 on a remote endpoint.

## Metadata

- Atomic GUID: 2e5eac3e-327b-4a88-a0c0-c4057039a8dd
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### password

- description: Password to authenticate with
- type: string
- default: At0micStrong

### target

- description: Target
- type: string
- default: localhost

### task_command

- description: What you want to execute
- type: string
- default: C:\windows\system32\cmd.exe

### time

- description: What time 24 Hour
- type: string
- default: 20:10

### user_name

- description: Username to authenticate with, format: DOMAIN\User
- type: string
- default: DOMAIN\user

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
SCHTASKS /Create /S #{target} /RU #{user_name} /RP #{password} /TN "Atomic task" /TR "#{task_command}" /SC daily /ST #{time}
```

### Cleanup

```cmd
SCHTASKS /Delete /S #{target} /U #{user_name} /P #{password} /TN "Atomic task" /F >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
