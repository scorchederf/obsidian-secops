---
atomic_guid: "d9efa6c7-6518-42b2-809a-4f2a8e242b9b"
title: "Create a Linux user via kubectl in a Pod"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "d9efa6c7-6518-42b2-809a-4f2a8e242b9b"
  - "Create a Linux user via kubectl in a Pod"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a Linux user via kubectl in a Pod

Launches a short-lived Alpine pod and creates a Linux user inside the pod.
The pod is automatically deleted after execution.

## Metadata

- Atomic GUID: d9efa6c7-6518-42b2-809a-4f2a8e242b9b
- Technique: T1136.001: Create Account: Local Account
- Platforms: containers
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Input Arguments

### image_name

- description: Name of the docker image
- type: string
- default: alpine

### pod_name

- description: K8s pod_name to execute the command in
- type: string
- default: atomic-linux-useradd

### username

- description: Username of the user to create inside the pod
- type: string
- default: evil_user

## Dependencies

kubectl must be installed and configured

### Prerequisite Check

```text
which kubectl
```

### Get Prerequisite

```text
echo "kubectl must be installed manually"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
kubectl run #{pod_name} --image=#{image_name} --restart=Never --rm -it -- sh -lc 'adduser -D #{username} && id #{username}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
