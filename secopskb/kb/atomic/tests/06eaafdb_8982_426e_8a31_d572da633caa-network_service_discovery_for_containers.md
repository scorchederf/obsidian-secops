---
atomic_guid: "06eaafdb-8982-426e-8a31-d572da633caa"
title: "Network Service Discovery for Containers"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "06eaafdb-8982-426e-8a31-d572da633caa"
  - "Network Service Discovery for Containers"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Service Discovery for Containers

Attackers may try to obtain a list of services that are operating on remote hosts and local network infrastructure devices, in order to identify potential vulnerabilities that can be exploited through remote software attacks. They typically use tools to conduct port and vulnerability scans in order to obtain this information.

## Metadata

- Atomic GUID: 06eaafdb-8982-426e-8a31-d572da633caa
- Technique: T1046: Network Service Discovery
- Platforms: containers
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

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
sudo systemctl status docker  --no-pager
```

### Get Prerequisite

```text
sudo systemctl start docker
```

## Executor

- name: sh

### Command

```sh
docker build -t t1046 $PathToAtomicsFolder/T1046/src/
docker run --name t1046_container --rm -d -t t1046
docker exec t1046_container /scan.sh
```

### Cleanup

```sh
docker stop t1046_container
docker rmi -f t1046
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
