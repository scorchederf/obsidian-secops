---
atomic_guid: "f3191b84-c38b-400b-867e-3a217a27795f"
title: "Windows - Stop service by killing process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "f3191b84-c38b-400b-867e-3a217a27795f"
  - "Windows - Stop service by killing process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stops a specified service killng the service's process.
This technique was used by WannaCry. Upon execution, if the spoolsv service was running "SUCCESS: The process "spoolsv.exe" with PID 2316 has been terminated."
will be displayed. If the service was not running "ERROR: The process "spoolsv.exe" not found." will be displayed and it can be
started by running the cleanup command.

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489: Service Stop]]

## Input Arguments

### process_name

- description: Name of a process to kill
- type: string
- default: spoolsv.exe

## Executor

- name: command_prompt

### Command

```cmd
taskkill.exe /f /im #{process_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
