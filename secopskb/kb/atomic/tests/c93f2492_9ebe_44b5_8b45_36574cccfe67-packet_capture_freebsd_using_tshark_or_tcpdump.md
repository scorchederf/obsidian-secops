---
atomic_guid: "c93f2492-9ebe-44b5-8b45-36574cccfe67"
title: "Packet Capture FreeBSD using tshark or tcpdump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c93f2492-9ebe-44b5-8b45-36574cccfe67"
  - "Packet Capture FreeBSD using tshark or tcpdump"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Packet Capture FreeBSD using tshark or tcpdump

Perform a PCAP. Wireshark will be required for tshark. TCPdump may already be installed.

Upon successful execution, tshark or tcpdump will execute and capture 5 packets on interface ens33.

## Metadata

- Atomic GUID: c93f2492-9ebe-44b5-8b45-36574cccfe67
- Technique: T1040: Network Sniffing
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Input Arguments

### interface

- description: Specify interface to perform PCAP on.
- type: string
- default: em0

## Dependencies

Check if at least one of tcpdump or tshark is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v tcpdump)" ] && [ ! -x "$(command -v tshark)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y wireshark-nox11)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
tcpdump -c 5 -nnni #{interface}
tshark -c 5 -i #{interface}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
