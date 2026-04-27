---
atomic_guid: "08b4718f-a8bf-4bb5-a552-294fc5178fea"
title: "Linux - Stop service by killing process using pkill"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "08b4718f-a8bf-4bb5-a552-294fc5178fea"
  - "Linux - Stop service by killing process using pkill"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Linux - Stop service by killing process using pkill

Stops a specified service by sending a SIGTERM signal to the linked process using pkill. This method is effective when multiple instances of the process may be running.
Upon execution, if any instances of the process were running, they will be terminated. If no instances were running, pkill will not find any processes to kill.
Stopped service can be restarted by running the cleanup command.
You can list all available services with following command: "systemctl list-units --type=service"

## Metadata

- Atomic GUID: 08b4718f-a8bf-4bb5-a552-294fc5178fea
- Technique: T1489: Service Stop
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1489/T1489.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Input Arguments

### process_pattern

- description: Pattern to match the name of the process to kill
- type: string
- default: ^cron$

### service_name

- description: Name of a service to restart
- type: string
- default: cron

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo pkill -SIGTERM #{process_pattern}
```

### Cleanup

```bash
sudo systemctl start #{service_name} 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
