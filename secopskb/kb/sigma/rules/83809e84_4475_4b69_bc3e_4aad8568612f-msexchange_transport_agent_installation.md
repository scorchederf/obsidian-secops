---
sigma_id: "83809e84-4475-4b69-bc3e-4aad8568612f"
title: "MSExchange Transport Agent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_msexchange_transport_agent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_msexchange_transport_agent.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "83809e84-4475-4b69-bc3e-4aad8568612f"
  - "MSExchange Transport Agent Installation"
attack_technique_ids:
  - "T1505.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSExchange Transport Agent Installation

Detects the Installation of a Exchange Transport Agent

## Metadata

- Rule ID: 83809e84-4475-4b69-bc3e-4aad8568612f
- Status: test
- Level: medium
- Author: Tobias Michalski (Nextron Systems)
- Date: 2021-06-08
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_msexchange_transport_agent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.002]]

## Detection

```yaml
selection:
  CommandLine|contains: Install-TransportAgent
condition: selection
```

## False Positives

- Legitimate installations of exchange TransportAgents. AssemblyPath is a good indicator for this.

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_msexchange_transport_agent.yml)
