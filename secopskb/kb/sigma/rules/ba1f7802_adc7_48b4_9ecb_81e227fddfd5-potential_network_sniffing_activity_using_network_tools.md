---
sigma_id: "ba1f7802-adc7-48b4-9ecb-81e227fddfd5"
title: "Potential Network Sniffing Activity Using Network Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_network_sniffing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_sniffing.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ba1f7802-adc7-48b4-9ecb-81e227fddfd5"
  - "Potential Network Sniffing Activity Using Network Tools"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Network Sniffing Activity Using Network Tools

Detects potential network sniffing via use of network tools such as "tshark", "windump".
Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection.
An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

## Metadata

- Rule ID: ba1f7802-adc7-48b4-9ecb-81e227fddfd5
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-21
- Modified: 2023-02-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_network_sniffing.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection_tshark:
  Image|endswith: \tshark.exe
  CommandLine|contains: -i
selection_windump:
  Image|endswith: \windump.exe
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activity to troubleshoot network issues

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1040/T1040.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_sniffing.yml)
