---
atomic_guid: "1a4ebe70-31d0-417b-ade2-ef4cb3e7d0e1"
title: "Remote System Discovery - ip route"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "1a4ebe70-31d0-417b-ade2-ef4cb3e7d0e1"
  - "Remote System Discovery - ip route"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use the ip route command to display the kernels routing tables.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Dependencies

Check if ip command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v ip)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
apt-get install iproute2 -y
```

## Executor

- name: sh

### Command

```bash
ip route show
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
