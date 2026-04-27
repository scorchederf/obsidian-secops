---
atomic_guid: "9ae28d3f-190f-4fa0-b023-c7bd3e0eabf2"
title: "System Network Connections Discovery FreeBSD, Linux & MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "9ae28d3f-190f-4fa0-b023-c7bd3e0eabf2"
  - "System Network Connections Discovery FreeBSD, Linux & MacOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get a listing of network connections.

Upon successful execution, sh will execute `netstat` and `who -a`. Results will output via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]

## Dependencies

Check if netstat command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v netstat)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
echo "Install netstat on the machine."; exit 1;
```

## Executor

- name: sh

### Command

```bash
netstat
who -a
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
