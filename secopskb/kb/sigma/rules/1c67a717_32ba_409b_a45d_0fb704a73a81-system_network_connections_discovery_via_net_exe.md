---
sigma_id: "1c67a717-32ba-409b-a45d-0fb704a73a81"
title: "System Network Connections Discovery Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_use_network_connections_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_network_connections_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "1c67a717-32ba-409b-a45d-0fb704a73a81"
  - "System Network Connections Discovery Via Net.EXE"
attack_technique_ids:
  - "T1049"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Network Connections Discovery Via Net.EXE

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network.

## Metadata

- Rule ID: 1c67a717-32ba-409b-a45d-0fb704a73a81
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-10
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_use_network_connections_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
- CommandLine|endswith:
  - ' use'
  - ' sessions'
- CommandLine|contains:
  - ' use '
  - ' sessions '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1049/T1049.md#atomic-test-1---system-network-connections-discovery

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_network_connections_discovery.yml)
