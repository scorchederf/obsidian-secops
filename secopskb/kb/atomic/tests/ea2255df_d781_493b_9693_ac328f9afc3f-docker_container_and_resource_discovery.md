---
atomic_guid: "ea2255df-d781-493b-9693-ac328f9afc3f"
title: "Docker Container and Resource Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1613"
attack_technique_name: "Container and Resource Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1613/T1613.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "ea2255df-d781-493b-9693-ac328f9afc3f"
  - "Docker Container and Resource Discovery"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Docker Container and Resource Discovery

Adversaries may attempt to discover containers and other resources that are available within a containers environment.

## Metadata

- Atomic GUID: ea2255df-d781-493b-9693-ac328f9afc3f
- Technique: T1613: Container and Resource Discovery
- Platforms: containers
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1613/T1613.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1613-container_and_resource_discovery|T1613]]

## Dependencies

Verify Docker is installed.

### Prerequisite Check

```bash
which docker
```

### Get Prerequisite

```bash
if [ "" == "`which docker`" ]; then echo "Docker Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install docker ; elif [ -n "`which yum`" ]; then sudo yum -y install docker ; fi ; else echo "Docker installed"; fi
```

Verify Docker service is running.

### Prerequisite Check

```bash
sudo systemctl status docker --no-pager
```

### Get Prerequisite

```bash
sudo systemctl start docker
```

## Executor

- name: sh

### Command

```bash
docker build -t t1613 $PathtoAtomicsFolder/T1613/src/
docker run --name t1613_container --rm -d -t t1613
docker ps
docker stats --no-stream
docker inspect $(docker ps -l -q --filter ancestor=t1613)
```

### Cleanup

```bash
docker stop t1613_container
docker rmi -f t1613
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1613/T1613.yaml)
