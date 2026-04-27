---
atomic_guid: "31e794c4-48fd-4a76-aca4-6587c155bc11"
title: "List All Secrets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.007"
attack_technique_name: "Kubernetes List Secrets"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "31e794c4-48fd-4a76-aca4-6587c155bc11"
  - "List All Secrets"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A Kubernetes secret is an object that lets users store and manage sensitive information, such as passwords and connection strings in the cluster. Secrets can be consumed by reference in the pod configuration. Attackers who have permissions to retrieve the secrets from the API server (by using the pod service account, for example) can access sensitive information that might include credentials to various services or provide further access to the cluster.
[More information about secrets](https://kubernetes.io/docs/concepts/configuration/secret/).

This test will make a request to the Kubernetes api at the `/api/v1/secrets` endpoint requesting every secret stored within the cluster.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552007-container-api|T1552.007: Container API]]

## Dependencies

kubectl must be installed

### Prerequisite Check

```untitled
which kubectl
```

### Get Prerequisite

```untitled
echo "kubectl not installed, please install kubectl (https://kubernetes.io/docs/tasks/tools/)"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
kubectl get secrets --all-namespaces
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml)
