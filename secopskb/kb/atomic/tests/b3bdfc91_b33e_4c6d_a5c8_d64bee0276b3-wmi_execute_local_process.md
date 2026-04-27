---
atomic_guid: "b3bdfc91-b33e-4c6d-a5c8-d64bee0276b3"
title: "WMI Execute Local Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "b3bdfc91-b33e-4c6d-a5c8-d64bee0276b3"
  - "WMI Execute Local Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses wmic.exe to execute a process on the local host.
When the test completes , a new process will be started locally .A notepad application will be started when input is left on default.

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Input Arguments

### process_to_execute

- description: Name or path of process to execute.
- type: string
- default: notepad.exe

## Executor

- name: command_prompt

### Command

```cmd
wmic process call create #{process_to_execute}
```

### Cleanup

```cmd
wmic process where name='#{process_to_execute}' delete >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
