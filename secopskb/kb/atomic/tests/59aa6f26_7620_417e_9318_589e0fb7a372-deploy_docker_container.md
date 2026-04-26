---
atomic_guid: "59aa6f26-7620-417e-9318-589e0fb7a372"
title: "Deploy Docker container"
framework: "atomic"
generated: "true"
attack_technique_id: "T1610"
attack_technique_name: "Deploy a container"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1610/T1610.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "59aa6f26-7620-417e-9318-589e0fb7a372"
  - "Deploy Docker container"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Deploy Docker container

Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime. They can do this using docker create and docker start commands. Kinsing & Doki was exploited using this technique.

## Metadata

- Atomic GUID: 59aa6f26-7620-417e-9318-589e0fb7a372
- Technique: T1610: Deploy a container
- Platforms: containers
- Executor: bash
- Dependency Executor: sh
- Source Path: atomics/T1610/T1610.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1610-deploy_container|T1610]]

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
sudo systemctl status docker  --no-pager
```

### Get Prerequisite

```bash
sudo systemctl start docker
```

## Executor

- name: bash

### Command

```bash
docker build -t t1610 $PathtoAtomicsFolder/T1610/src/
docker run --name t1610_container --rm -itd t1610 bash /tmp/script.sh
```

### Cleanup

```bash
docker stop t1610_container
docker rmi -f t1610:latest
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1610/T1610.yaml)
