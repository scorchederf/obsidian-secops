---
atomic_guid: "7e46c7a5-0142-45be-a858-1a3ecb4fd3cb"
title: "List opened files by user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "7e46c7a5-0142-45be-a858-1a3ecb4fd3cb"
  - "List opened files by user"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

List opened files by user

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]

## Dependencies

check if lsof exists

### Prerequisite Check

```bash
which lsof
```

### Get Prerequisite

```bash
(which pkg && pkg install -y lsof)||(which yum && yum -y install lsof)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y lsof)
```

## Executor

- name: sh

### Command

```bash
username=$(id -u -n) && lsof -u $username
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
