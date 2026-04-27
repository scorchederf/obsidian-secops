---
atomic_guid: "7fe741f7-b265-4951-a7c7-320889083b3e"
title: "Packet Capture Linux using tshark or tcpdump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "7fe741f7-b265-4951-a7c7-320889083b3e"
  - "Packet Capture Linux using tshark or tcpdump"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Packet Capture Linux using tshark or tcpdump

Perform a PCAP. Wireshark will be required for tshark. TCPdump may already be installed.

Upon successful execution, tshark or tcpdump will execute and capture 5 packets on interface ens33.

## Metadata

- Atomic GUID: 7fe741f7-b265-4951-a7c7-320889083b3e
- Technique: T1040: Network Sniffing
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Input Arguments

### interface

- description: Specify interface to perform PCAP on.
- type: string
- default: ens33

## Dependencies

Check if at least one of tcpdump or tshark is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v tcpdump)" ] && [ ! -x "$(command -v tshark)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install epel-release tcpdump tshark)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y tcpdump tshark)
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
tcpdump -c 5 -nnni #{interface}
tshark -c 5 -i #{interface}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
