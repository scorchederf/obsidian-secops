---
atomic_guid: "e6fe5095-545d-4c8b-a0ae-e863914be3aa"
title: "Packet Capture macOS using /dev/bpfN with sudo"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "e6fe5095-545d-4c8b-a0ae-e863914be3aa"
  - "Packet Capture macOS using /dev/bpfN with sudo"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Packet Capture macOS using /dev/bpfN with sudo

Opens a /dev/bpf file (O_RDONLY) and captures packets for a few seconds.

## Metadata

- Atomic GUID: e6fe5095-545d-4c8b-a0ae-e863914be3aa
- Technique: T1040: Network Sniffing
- Platforms: macos
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
- default: PathToAtomicsFolder/T1040/src/macos_pcapdemo.c

### ifname

- description: Specify interface to perform PCAP on.
- type: string
- default: en0

### program_path

- description: Path to compiled C program
- type: string
- default: /tmp/t1040_macos_pcapdemo

## Dependencies

compile C program

### Prerequisite Check

```text
exit 1
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
sudo #{program_path} -i #{ifname} -t 3
```

### Cleanup

```bash
rm -f #{program_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
