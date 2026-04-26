---
atomic_guid: "788e0019-a483-45da-bcfe-96353d46820f"
title: "Cat the contents of a Kubernetes service account token file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.007"
attack_technique_name: "Kubernetes List Secrets"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "788e0019-a483-45da-bcfe-96353d46820f"
  - "Cat the contents of a Kubernetes service account token file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cat the contents of a Kubernetes service account token file

Access the Kubernetes service account access token stored within a container in a cluster.

## Metadata

- Atomic GUID: 788e0019-a483-45da-bcfe-96353d46820f
- Technique: T1552.007: Kubernetes List Secrets
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1552.007/T1552.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

## Dependencies

Verify docker is installed.

### Prerequisite Check

```bash
which docker
```

### Get Prerequisite

```bash
if [ "" == "`which docker`" ]; then echo "Docker Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install docker ; elif [ -n "`which yum`" ]; then sudo yum -y install docker ; fi ; else echo "Docker installed"; fi
```

Verify docker service is running.

### Prerequisite Check

```bash
sudo systemctl status docker
```

### Get Prerequisite

```bash
sudo systemctl start docker
```

Verify kind is in the path.

### Prerequisite Check

```bash
which kind
```

### Get Prerequisite

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
chmod +x ./kind
mv kind /usr/bin/kind
```

Verify kind-atomic-cluster is created

### Prerequisite Check

```bash
sudo kind get clusters
```

### Get Prerequisite

```bash
sudo kind create cluster --name atomic-cluster
```

Verify kubectl is in path

### Prerequisite Check

```bash
which kubectl
```

### Get Prerequisite

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
mv kubectl /usr/bin/kubectl
```

Verify atomic-pod is running.

### Prerequisite Check

```bash
kubectl --context kind-atomic-cluster get pods |grep atomic-pod
```

### Get Prerequisite

```bash
kubectl --context kind-atomic-cluster run atomic-pod --image=alpine --command -- sleep infinity
```

## Executor

- name: sh

### Command

```bash
kubectl --context kind-atomic-cluster exec atomic-pod -- cat /run/secrets/kubernetes.io/serviceaccount/token
```

### Cleanup

```bash
kubectl --context kind-atomic-cluster delete pod atomic-pod
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.007/T1552.007.yaml)
