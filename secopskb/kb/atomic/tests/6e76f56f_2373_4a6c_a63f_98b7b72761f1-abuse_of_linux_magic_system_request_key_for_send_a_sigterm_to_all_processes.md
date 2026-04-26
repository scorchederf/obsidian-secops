---
atomic_guid: "6e76f56f-2373-4a6c-a63f-98b7b72761f1"
title: "Abuse of linux magic system request key for Send a SIGTERM to all processes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1489"
attack_technique_name: "Service Stop"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "6e76f56f-2373-4a6c-a63f-98b7b72761f1"
  - "Abuse of linux magic system request key for Send a SIGTERM to all processes"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abuse of linux magic system request key for Send a SIGTERM to all processes

Adversaries with root or sufficient privileges Send a SIGTERM to all processes, except for init. By writing 'e' to /proc/sysrq-trigger, they can forced kill all processes, except for init.

## Metadata

- Atomic GUID: 6e76f56f-2373-4a6c-a63f-98b7b72761f1
- Technique: T1489: Service Stop
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1489/T1489.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "e" > /proc/sysrq-trigger
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1489/T1489.yaml)
