---
atomic_guid: "0d5a2b03-3a26-45e4-96ae-89485b4d1f97"
title: "Port Scan using nmap (Port range)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "0d5a2b03-3a26-45e4-96ae-89485b4d1f97"
  - "Port Scan using nmap (Port range)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Port Scan using nmap (Port range)

Scan multiple ports to check for listening ports with nmap

## Metadata

- Atomic GUID: 0d5a2b03-3a26-45e4-96ae-89485b4d1f97
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

- description: Host(s) to scan.
- type: string
- default: 127.0.0.1

### port_range

- description: Port range(s) to scan.
- type: string
- default: 0-65535

## Dependencies

Check if nmap command exists on the machine

### Prerequisite Check

```text
if [ -x "$(command -v nmap)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
(which yum && yum -y install epel-release nmap)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y nmap)||(which pkg && pkg install -y nmap)||(which brew && brew install nmap)
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
nmap -Pn -sV -p #{port_range} #{host}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
