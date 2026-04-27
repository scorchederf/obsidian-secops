---
atomic_guid: "fc631702-3f03-4f2b-8d8a-6b3d055580a1"
title: "Podman Container and Resource Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1613"
attack_technique_name: "Container and Resource Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1613/T1613.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "fc631702-3f03-4f2b-8d8a-6b3d055580a1"
  - "Podman Container and Resource Discovery"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries may attempt to discover containers and other resources that are available within a containers environment.

## ATT&CK Mapping

- [[kb/attack/techniques/T1613-container_and_resource_discovery|T1613: Container and Resource Discovery]]

## Dependencies

Verify Podman is installed.

### Prerequisite Check

```bash
which podman
```

### Get Prerequisite

```bash
if [ "" == "`which podman`" ]; then echo "Podman Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install podman ; elif [ -n "`which yum`" ]; then sudo yum -y install podman ; elif [ -n "`which pacman`" ]; then sudo pacman -Sy podman --noconfirm ; elif [ -n "`which brew`" ]; then brew install podman ; else echo "Unsupported package manager"; fi ; else echo "Podman installed"; fi
```

Verify Podman service is running.

### Prerequisite Check

```bash
sudo systemctl status podman --no-pager
```

### Get Prerequisite

```bash
sudo systemctl start podman
```

## Executor

- name: sh

### Command

```bash
podman build -t t1613 $PathtoAtomicsFolder/T1613/src/
podman run --name t1613_container --rm -d -t t1613
podman ps
podman stats --no-stream
podman inspect $(podman ps -l -q --filter ancestor=t1613)
```

### Cleanup

```bash
podman stop t1613_container
podman rmi -f t1613
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1613/T1613.yaml)
