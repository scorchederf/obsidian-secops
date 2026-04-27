---
atomic_guid: "e5d95be6-02ee-4ff1-aebe-cf86013b6189"
title: "Linux - Stop service by killing process using killall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "e5d95be6-02ee-4ff1-aebe-cf86013b6189"
  - "Linux - Stop service by killing process using killall"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stops a specified service by sending a SIGTERM signal to the linked process using the killall command.
Upon execution, if the service's main process was running, it will be terminated.
If the service was not running, no process will be found to kill and it can be restarted by running the cleanup command.
You can list all available services with following command: "systemctl list-units --type=service"

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489: Service Stop]]

## Input Arguments

### process_name

- description: Name of a process to stop
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

```bash
sudo killall -SIGTERM #{process_name}
```

### Cleanup

```bash
sudo systemctl start #{service_name} 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
