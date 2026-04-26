---
atomic_guid: "b1cbdf8b-6078-48f5-a890-11ea19d7f8e9"
title: "Packet Capture Linux socket AF_PACKET,SOCK_RAW with BPF filter for UDP with sudo"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "b1cbdf8b-6078-48f5-a890-11ea19d7f8e9"
  - "Packet Capture Linux socket AF_PACKET,SOCK_RAW with BPF filter for UDP with sudo"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Packet Capture Linux socket AF_PACKET,SOCK_RAW with BPF filter for UDP with sudo

Captures packets with domain=AF_PACKET,type=SOCK_RAW for a few seconds.
Sets a BPF filter on the socket to filter for UDP traffic.

## Metadata

- Atomic GUID: b1cbdf8b-6078-48f5-a890-11ea19d7f8e9
- Technique: T1040: Network Sniffing
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Input Arguments

### csource_path

- description: Path to C program source
- type: string
- default: PathToAtomicsFolder/T1040/src/linux_pcapdemo.c

### program_path

- description: Path to compiled C program
- type: string
- default: /tmp/t1040_linux_pcapdemo

## Dependencies

compile C program

### Prerequisite Check

```text
if [ -f "#{program_path}" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
cc #{csource_path} -o #{program_path}
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo #{program_path} -a -f -t 3
```

### Cleanup

```bash
rm -f #{program_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
