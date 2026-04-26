---
atomic_guid: "a3a0d4c9-c068-4563-a08d-583bd05b884c"
title: "Filtered Packet Capture FreeBSD using /dev/bpfN with sudo"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "a3a0d4c9-c068-4563-a08d-583bd05b884c"
  - "Filtered Packet Capture FreeBSD using /dev/bpfN with sudo"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Filtered Packet Capture FreeBSD using /dev/bpfN with sudo

Opens a /dev/bpf file (O_RDONLY), sets BPF filter for 'udp' and captures packets for a few seconds.

## Metadata

- Atomic GUID: a3a0d4c9-c068-4563-a08d-583bd05b884c
- Technique: T1040: Network Sniffing
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Input Arguments

### csource_path

- description: Path to C program source
- type: string
- default: PathToAtomicsFolder/T1040/src/freebsd_pcapdemo.c

### ifname

- description: Specify interface to perform PCAP on.
- type: string
- default: em0

### program_path

- description: Path to compiled C program
- type: string
- default: /tmp/t1040_freebsd_pcapdemo

## Dependencies

compile C program

### Prerequisite Check

```bash
exit 1
```

### Get Prerequisite

```bash
cc #{csource_path} -o #{program_path}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo #{program_path} -f -i #{ifname} -t 3
```

### Cleanup

```bash
rm -f #{program_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
