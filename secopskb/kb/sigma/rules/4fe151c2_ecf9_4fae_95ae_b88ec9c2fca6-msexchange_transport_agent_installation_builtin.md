---
sigma_id: "4fe151c2-ecf9-4fae-95ae-b88ec9c2fca6"
title: "MSExchange Transport Agent Installation - Builtin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_transportagent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_transportagent.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / msexchange-management"
aliases:
  - "4fe151c2-ecf9-4fae-95ae-b88ec9c2fca6"
  - "MSExchange Transport Agent Installation - Builtin"
attack_technique_ids:
  - "T1505.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSExchange Transport Agent Installation - Builtin

Detects the Installation of a Exchange Transport Agent

## Metadata

- Rule ID: 4fe151c2-ecf9-4fae-95ae-b88ec9c2fca6
- Status: test
- Level: medium
- Author: Tobias Michalski (Nextron Systems)
- Date: 2021-06-08
- Modified: 2022-11-27
- Source Path: rules/windows/builtin/msexchange/win_exchange_transportagent.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.002]]

## Detection

```yaml
selection:
- Install-TransportAgent
condition: selection
```

## False Positives

- Legitimate installations of exchange TransportAgents. AssemblyPath is a good indicator for this.

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_transportagent.yml)
