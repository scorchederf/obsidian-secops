---
atomic_guid: "9ddf2e5e-7e2c-46c2-9940-3c2ff29c7213"
title: "At - Schedule a job via kubectl in a Pod"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.002"
attack_technique_name: "Scheduled Task/Job: At"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.002/T1053.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "9ddf2e5e-7e2c-46c2-9940-3c2ff29c7213"
  - "At - Schedule a job via kubectl in a Pod"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# At - Schedule a job via kubectl in a Pod

Launches a short-lived Ubuntu pod, installs the `at` utility, starts the `atd` daemon,
and submits a job with `at`. The pod is deleted after execution.

## Metadata

- Atomic GUID: 9ddf2e5e-7e2c-46c2-9940-3c2ff29c7213
- Technique: T1053.002: Scheduled Task/Job: At
- Platforms: containers
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1053.002/T1053.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Input Arguments

### at_command

- description: The command to be run
- type: string
- default: echo Hello from Atomic Red Team

### image_name

- description: Name of the image
- type: string
- default: ubuntu

### pod_name

- description: K8s pod name to execute the command in
- type: string
- default: atomic-at-schedule

### time_spec

- description: Time specification of when the command should run
- type: string
- default: now + 1 minute

## Dependencies

kubectl must be installed and configured

### Prerequisite Check

```untitled
which kubectl
```

### Get Prerequisite

```untitled
echo "kubectl must be installed manually"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
kubectl run #{pod_name} --image=#{image_name} --restart=Never --attach --rm -i -- bash -lc "apt-get update -y >/dev/null 2>&1 && apt-get install -y at >/dev/null 2>&1 && (atd || /usr/sbin/atd) && echo '#{at_command}' | at #{time_spec} && at -l"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.002/T1053.002.yaml)
