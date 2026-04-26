---
atomic_guid: "42e3a5bd-1e45-427f-aa08-2a65fa29a820"
title: "Linux - Stop service using systemctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "42e3a5bd-1e45-427f-aa08-2a65fa29a820"
  - "Linux - Stop service using systemctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux - Stop service using systemctl

Stops a specified service using the systemctl command.
Upon execution, if the specified service was running, it will change to a state of inactive and it can be restarted by running the cleanup command.
You can list all available services with following command: "systemctl list-units --type=service"

## Metadata

- Atomic GUID: 42e3a5bd-1e45-427f-aa08-2a65fa29a820
- Technique: T1489: Service Stop
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1489/T1489.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Input Arguments

### service_name

- description: Name of a service to stop
- type: string
- default: cron

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo systemctl stop #{service_name}
```

### Cleanup

```sh
sudo systemctl start #{service_name} 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
