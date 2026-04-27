---
atomic_guid: "900e2c49-221b-42ec-ae3c-4717e41e6219"
title: "Docker Exec Into Container"
framework: "atomic"
generated: "true"
attack_technique_id: "T1609"
attack_technique_name: "Kubernetes Exec Into Container"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1609/T1609.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "900e2c49-221b-42ec-ae3c-4717e41e6219"
  - "Docker Exec Into Container"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attackers who have permissions, can run malicious commands in containers in the cluster using exec command (“docker exec”). In this method, attackers can use legitimate images, such as an OS image (e.g., Ubuntu) as a backdoor container, and run their malicious code remotely by using “docker exec”. Kinsing (Golang-based malware) was executed with an Ubuntu container entry point that runs shell scripts.

## ATT&CK Mapping

- [[kb/attack/techniques/T1609-container_administration_command|T1609: Container Administration Command]]

## Dependencies

docker must be installed

### Prerequisite Check

```untitled
which docker
```

### Get Prerequisite

```untitled
if [ "" == "`which docker`" ]; then echo "Docker Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install docker ; elif [ -n "`which yum`" ]; then sudo yum -y install docker ; fi ; else echo "Docker installed"; fi
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
docker build -t t1609  $PathtoAtomicsFolder/T1609/src/ 
docker run --name t1609_container --rm -itd t1609 bash /tmp/script.sh
docker exec -i t1609_container bash -c "cat /tmp/output.txt"
```

### Cleanup

```bash
docker stop t1609_container
docker rmi -f t1609:latest
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1609/T1609.yaml)
