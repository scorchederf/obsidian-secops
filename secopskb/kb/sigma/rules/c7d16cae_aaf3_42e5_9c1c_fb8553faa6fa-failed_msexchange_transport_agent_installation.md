---
sigma_id: "c7d16cae-aaf3-42e5-9c1c-fb8553faa6fa"
title: "Failed MSExchange Transport Agent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_transportagent_failed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_transportagent_failed.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / msexchange-management"
aliases:
  - "c7d16cae-aaf3-42e5-9c1c-fb8553faa6fa"
  - "Failed MSExchange Transport Agent Installation"
attack_technique_ids:
  - "T1505.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Failed MSExchange Transport Agent Installation

Detects a failed installation of a Exchange Transport Agent

## Metadata

- Rule ID: c7d16cae-aaf3-42e5-9c1c-fb8553faa6fa
- Status: test
- Level: high
- Author: Tobias Michalski (Nextron Systems)
- Date: 2021-06-08
- Modified: 2022-07-12
- Source Path: rules/windows/builtin/msexchange/win_exchange_transportagent_failed.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.002]]

## Detection

```yaml
selection:
  EventID: 6
  Data|contains: Install-TransportAgent
condition: selection
```

## False Positives

- Legitimate installations of exchange TransportAgents. AssemblyPath is a good indicator for this.

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=8

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_transportagent_failed.yml)
