---
sigma_id: "a29c1813-ab1f-4dde-b489-330b952e91ae"
title: "Suspicious Network Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_network_command.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_command.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "a29c1813-ab1f-4dde-b489-330b952e91ae"
  - "Suspicious Network Command"
attack_technique_ids:
  - "T1016"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Network Command

Adversaries may look for details about the network configuration and settings of systems they access or through information discovery of remote systems

## Metadata

- Rule ID: a29c1813-ab1f-4dde-b489-330b952e91ae
- Status: test
- Level: low
- Author: frack113, Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
- Date: 2021-12-07
- Modified: 2025-10-19
- Source Path: rules/windows/process_creation/proc_creation_win_susp_network_command.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Detection

```yaml
selection:
  CommandLine|re:
  - ipconfig\s+/all
  - netsh\s+interface show interface
  - arp\s+-a
  - nbtstat\s+-n
  - net\s+config
  - route\s+print
condition: selection
```

## False Positives

- Administrator, hotline ask to user

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T1016.md#atomic-test-1---system-network-configuration-discovery-on-windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_command.yml)
