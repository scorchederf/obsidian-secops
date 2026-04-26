---
atomic_guid: "332f4c76-7e96-41a6-8cc2-7361c49db8be"
title: "Linux - Stop service by killing process using kill"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "332f4c76-7e96-41a6-8cc2-7361c49db8be"
  - "Linux - Stop service by killing process using kill"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux - Stop service by killing process using kill

Stops a specified service by sending a SIGTERM signal to the linked process using the kill command. Upon execution, if the service's main process was running, it will be terminated.
If the service was not running, no process will be found to kill and it can be restarted by running the cleanup command.
You can list all available services with following command: "systemctl list-units --type=service"

## Metadata

- Atomic GUID: 332f4c76-7e96-41a6-8cc2-7361c49db8be
- Technique: T1489: Service Stop
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1489/T1489.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Input Arguments

### process_name

- description: Name of a process to kill
- type: string
- default: cron

### service_name

- description: Name of a service to restart
- type: string
- default: cron

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo kill -SIGTERM $(pgrep #{process_name})
```

### Cleanup

```sh
sudo systemctl start #{service_name} 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
