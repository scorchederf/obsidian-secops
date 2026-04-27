---
atomic_guid: "d03bfcd3-ed87-49c8-8880-44bb772dea4b"
title: "ExecIntoContainer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1609"
attack_technique_name: "Kubernetes Exec Into Container"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1609/T1609.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "d03bfcd3-ed87-49c8-8880-44bb772dea4b"
  - "ExecIntoContainer"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attackers who have permissions, can run malicious commands in containers in the cluster using exec command (“kubectl exec”). In this method, attackers can use legitimate images, such as an OS image (e.g., Ubuntu) as a backdoor container, and run their malicious code remotely by using “kubectl exec”.

## ATT&CK Mapping

- [[kb/attack/techniques/T1609-container_administration_command|T1609: Container Administration Command]]

## Input Arguments

### command

- description: Command to run
- type: string
- default: uname

### namespace

- description: K8s namespace to use
- type: string
- default: default

### path

- description: Path to busybox.yaml file
- type: string
- default: $PathtoAtomicsFolder/T1609/src/busybox.yaml

## Dependencies

kubectl must be installed

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
kubectl create -f #{path} -n #{namespace}
# wait 3 seconds for the instance to come up
sleep 3
kubectl exec -n #{namespace} busybox -- #{command}
```

### Cleanup

```bash
kubectl delete pod busybox -n #{namespace}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1609/T1609.yaml)
