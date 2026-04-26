---
sigma_id: "4c519226-f0cd-4471-bd2f-6fbb2bb68a79"
title: "System Network Connections Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_system_network_connections_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_network_connections_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "4c519226-f0cd-4471-bd2f-6fbb2bb68a79"
  - "System Network Connections Discovery - Linux"
attack_technique_ids:
  - "T1049"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Network Connections Discovery - Linux

Detects usage of system utilities to discover system network connections

## Metadata

- Rule ID: 4c519226-f0cd-4471-bd2f-6fbb2bb68a79
- Status: test
- Level: low
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2023-01-17
- Source Path: rules/linux/process_creation/proc_creation_lnx_system_network_connections_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Detection

```yaml
selection:
  Image|endswith:
  - /who
  - /w
  - /last
  - /lsof
  - /netstat
filter_landscape_sysinfo:
  ParentCommandLine|contains: /usr/bin/landscape-sysinfo
  Image|endswith: /who
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1049/T1049.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_network_connections_discovery.yml)
