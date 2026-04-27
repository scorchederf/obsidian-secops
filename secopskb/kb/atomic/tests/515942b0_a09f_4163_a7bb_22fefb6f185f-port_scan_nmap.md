---
atomic_guid: "515942b0-a09f-4163-a7bb-22fefb6f185f"
title: "Port Scan Nmap"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "515942b0-a09f-4163-a7bb-22fefb6f185f"
  - "Port Scan Nmap"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Port Scan Nmap

Scan ports to check for listening ports with Nmap.
Upon successful execution, sh will utilize nmap, telnet, and nc to contact a single or range of addresses on port 80 to determine if listening. Results will be via stdout.

## Metadata

- Atomic GUID: 515942b0-a09f-4163-a7bb-22fefb6f185f
- Technique: T1046: Network Service Discovery
- Platforms: linux, macos
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Input Arguments

### host

- description: Host to scan.
- type: string
- default: 192.168.1.1

### network_range

- description: Network Range to Scan.
- type: string
- default: 192.168.1.0/24

### port

- description: Ports to scan.
- type: string
- default: 80

## Dependencies

Check if nmap command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v nmap)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install epel-release nmap)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y nmap)||(which pkg && pkg install -y nmap)
```

Check if nc command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v nc)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install epel-release nc)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y netcat)||(which pkg && pkg install -y netcat)
```

Check if telnet command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v telnet)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install epel-release telnet)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y telnet)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo nmap -sS #{network_range} -p #{port}
telnet #{host} #{port}
nc -nv #{host} #{port}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
