---
atomic_guid: "21dfb440-830d-4c86-a3e5-2a491d5a8d04"
title: "Windows - Stop service using Service Controller"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "21dfb440-830d-4c86-a3e5-2a491d5a8d04"
  - "Windows - Stop service using Service Controller"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Stop service using Service Controller

Stops a specified service using the sc.exe command. Upon execution, if the spooler service was running infomration will be displayed saying
it has changed to a state of STOP_PENDING. If the spooler service was not running "The service has not been started." will be displayed and it can be
started by running the cleanup command.

## Metadata

- Atomic GUID: 21dfb440-830d-4c86-a3e5-2a491d5a8d04
- Technique: T1489: Service Stop
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1489/T1489.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Input Arguments

### service_name

- description: Name of a service to stop
- type: string
- default: spooler

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc.exe stop #{service_name}
```

### Cleanup

```cmd
sc.exe start #{service_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
