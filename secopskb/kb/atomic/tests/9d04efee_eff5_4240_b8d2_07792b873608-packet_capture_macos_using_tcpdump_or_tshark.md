---
atomic_guid: "9d04efee-eff5-4240-b8d2-07792b873608"
title: "Packet Capture macOS using tcpdump or tshark"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "9d04efee-eff5-4240-b8d2-07792b873608"
  - "Packet Capture macOS using tcpdump or tshark"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Packet Capture macOS using tcpdump or tshark

Perform a PCAP on macOS. This will require Wireshark/tshark to be installed. TCPdump may already be installed.

Upon successful execution, tshark or tcpdump will execute and capture 5 packets on interface en0A.

## Metadata

- Atomic GUID: 9d04efee-eff5-4240-b8d2-07792b873608
- Technique: T1040: Network Sniffing
- Platforms: macos
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
- default: en0A

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
sudo tcpdump -c 5 -nnni #{interface}    
if [ -x "$(command -v tshark)" ]; then sudo tshark -c 5 -i #{interface}; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
