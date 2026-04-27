---
atomic_guid: "007d7aa4-8c4d-4f55-ba6a-7c965d51219c"
title: "Permission Groups Discovery for Containers- Local Groups"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "007d7aa4-8c4d-4f55-ba6a-7c965d51219c"
  - "Permission Groups Discovery for Containers- Local Groups"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attackers may try to obtain a list of services that are operating on remote hosts and local network infrastructure devices, in order to identify potential vulnerabilities that can be exploited through remote software attacks. They typically use tools to conduct port and vulnerability scans in order to obtain this information.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

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

- name: sh

### Command

```bash
docker build -t t1069 $PathtoAtomicsFolder/T1069.001/src/
docker run --name t1069_container --rm -d -t t1069
docker exec t1069_container ./test.sh
```

### Cleanup

```bash
docker stop t1069_container
docker rmi -f t1069
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
