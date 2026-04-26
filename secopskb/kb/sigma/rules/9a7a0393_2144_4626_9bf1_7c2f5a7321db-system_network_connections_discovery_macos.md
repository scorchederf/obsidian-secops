---
sigma_id: "9a7a0393-2144-4626-9bf1-7c2f5a7321db"
title: "System Network Connections Discovery - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_system_network_connections_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_network_connections_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "9a7a0393-2144-4626-9bf1-7c2f5a7321db"
  - "System Network Connections Discovery - MacOs"
attack_technique_ids:
  - "T1049"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Network Connections Discovery - MacOs

Detects usage of system utilities to discover system network connections

## Metadata

- Rule ID: 9a7a0393-2144-4626-9bf1-7c2f5a7321db
- Status: test
- Level: informational
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2022-12-28
- Source Path: rules/macos/process_creation/proc_creation_macos_system_network_connections_discovery.yml

## Logsource

- category: process_creation
- product: macos

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
condition: selection
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1049/T1049.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_system_network_connections_discovery.yml)
