---
atomic_guid: "ddfb0bc1-3c3f-47e9-a298-550ecfefacbd"
title: "ListCronjobs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.007"
attack_technique_name: "Kubernetes Cronjob"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.007/T1053.007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "ddfb0bc1-3c3f-47e9-a298-550ecfefacbd"
  - "ListCronjobs"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ListCronjobs

Kubernetes Job is a controller that creates one or more pods and ensures that a specified number of them successfully terminate. Kubernetes Job can be used to run containers that perform finite tasks for batch jobs. Kubernetes CronJob is used to schedule Jobs. Attackers may use Kubernetes CronJob for scheduling execution of malicious code that would run as a container in the cluster.

## Metadata

- Atomic GUID: ddfb0bc1-3c3f-47e9-a298-550ecfefacbd
- Technique: T1053.007: Kubernetes Cronjob
- Platforms: containers
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1053.007/T1053.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.007]]

## Input Arguments

### namespace

- description: K8s namespace to list
- type: string
- default: default

## Dependencies

kubectl must be installed

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
kubectl get cronjobs -n #{namespace}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.007/T1053.007.yaml)
