---
atomic_guid: "41274289-ec9c-4213-bea4-e43c4aa57954"
title: "Windows - Stop service using net.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "41274289-ec9c-4213-bea4-e43c4aa57954"
  - "Windows - Stop service using net.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stops a specified service using the net.exe command. Upon execution, if the service was running "The Print Spooler service was stopped successfully."
will be displayed. If the service was not running, "The Print Spooler service is not started." will be displayed and it can be
started by running the cleanup command.

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489: Service Stop]]

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
net.exe stop #{service_name}
```

### Cleanup

```cmd
net.exe start #{service_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
