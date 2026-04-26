---
sigma_id: "f4d3748a-65d1-4806-bd23-e25728081d01"
title: "Network Sniffing - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_network_sniffing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_network_sniffing.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "f4d3748a-65d1-4806-bd23-e25728081d01"
  - "Network Sniffing - Linux"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Sniffing - Linux

Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection.
An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

## Metadata

- Rule ID: f4d3748a-65d1-4806-bd23-e25728081d01
- Status: test
- Level: low
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2022-12-18
- Source Path: rules/linux/auditd/execve/lnx_auditd_network_sniffing.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection_1:
  type: execve
  a0: tcpdump
  a1: -c
  a3|contains: -i
selection_2:
  type: execve
  a0: tshark
  a1: -c
  a3: -i
condition: 1 of selection_*
```

## False Positives

- Legitimate administrator or user uses network sniffing tool for legitimate reasons.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1040/T1040.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_network_sniffing.yml)
