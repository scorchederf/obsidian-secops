---
atomic_guid: "43c3a49d-d15c-45e6-b303-f6e177e44a9a"
title: "ListSecrets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.007"
attack_technique_name: "Kubernetes List Secrets"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "43c3a49d-d15c-45e6-b303-f6e177e44a9a"
  - "ListSecrets"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ListSecrets

A Kubernetes secret is an object that lets users store and manage sensitive information, such as passwords and connection strings in the cluster. Secrets can be consumed by reference in the pod configuration. Attackers who have permissions to retrieve the secrets from the API server (by using the pod service account, for example) can access sensitive information that might include credentials to various services.

## Metadata

- Atomic GUID: 43c3a49d-d15c-45e6-b303-f6e177e44a9a
- Technique: T1552.007: Kubernetes List Secrets
- Platforms: containers
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1552.007/T1552.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

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
kubectl get secrets -n #{namespace}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml)
