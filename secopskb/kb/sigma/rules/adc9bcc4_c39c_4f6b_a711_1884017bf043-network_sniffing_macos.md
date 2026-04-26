---
sigma_id: "adc9bcc4-c39c-4f6b-a711-1884017bf043"
title: "Network Sniffing - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_network_sniffing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_network_sniffing.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "adc9bcc4-c39c-4f6b-a711-1884017bf043"
  - "Network Sniffing - MacOs"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Sniffing - MacOs

Detects the usage of tooling to sniff network traffic.
An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

## Metadata

- Rule ID: adc9bcc4-c39c-4f6b-a711-1884017bf043
- Status: test
- Level: informational
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-14
- Modified: 2022-11-26
- Source Path: rules/macos/process_creation/proc_creation_macos_network_sniffing.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection:
  Image|endswith:
  - /tcpdump
  - /tshark
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1040/T1040.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_network_sniffing.yml)
