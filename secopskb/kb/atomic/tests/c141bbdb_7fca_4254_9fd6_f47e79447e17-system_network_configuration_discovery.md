---
atomic_guid: "c141bbdb-7fca-4254-9fd6-f47e79447e17"
title: "System Network Configuration Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c141bbdb-7fca-4254-9fd6-f47e79447e17"
  - "System Network Configuration Discovery"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Configuration Discovery

Identify network configuration information.
Upon successful execution, sh will spawn multiple commands and output will be via stdout.

## Metadata

- Atomic GUID: c141bbdb-7fca-4254-9fd6-f47e79447e17
- Technique: T1016: System Network Configuration Discovery
- Platforms: macos, linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Dependencies

Check if arp command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v arp)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install net-tools)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools)
```

## Executor

- name: sh

### Command

```bash
if [ "$(uname)" = 'FreeBSD' ]; then cmd="netstat -Sp tcp"; else cmd="netstat -ant"; fi;
if [ -x "$(command -v arp)" ]; then arp -a; else echo "arp is missing from the machine. skipping..."; fi;
if [ -x "$(command -v ifconfig)" ]; then ifconfig; else echo "ifconfig is missing from the machine. skipping..."; fi;
if [ -x "$(command -v ip)" ]; then ip addr; else echo "ip is missing from the machine. skipping..."; fi;
if [ -x "$(command -v netstat)" ]; then $cmd | awk '{print $NF}' | grep -v '[[:lower:]]' | sort | uniq -c; else echo "netstat is missing from the machine. skipping..."; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
