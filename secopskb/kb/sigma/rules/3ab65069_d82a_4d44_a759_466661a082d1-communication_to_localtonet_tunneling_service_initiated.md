---
sigma_id: "3ab65069-d82a-4d44-a759-466661a082d1"
title: "Communication To LocaltoNet Tunneling Service Initiated"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_localtonet_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_localtonet_tunnel.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "3ab65069-d82a-4d44-a759-466661a082d1"
  - "Communication To LocaltoNet Tunneling Service Initiated"
attack_technique_ids:
  - "T1572"
  - "T1090"
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Communication To LocaltoNet Tunneling Service Initiated

Detects an executable initiating a network connection to "LocaltoNet" tunneling sub-domains.
LocaltoNet is a reverse proxy that enables localhost services to be exposed to the Internet.
Attackers have been seen to use this service for command-and-control activities to bypass MFA and perimeter controls.

## Metadata

- Rule ID: 3ab65069-d82a-4d44-a759-466661a082d1
- Status: test
- Level: high
- Author: Andreas Braathen (mnemonic.io)
- Date: 2024-06-17
- Source Path: rules/windows/network_connection/net_connection_win_domain_localtonet_tunnel.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1090-proxy|T1090]]
- [[kb/attack/techniques/T1102-web_service|T1102]]

## Detection

```yaml
selection:
  DestinationHostname|endswith:
  - .localto.net
  - .localtonet.com
  Initiated: 'true'
condition: selection
```

## False Positives

- Legitimate use of the LocaltoNet service.

## References

- https://localtonet.com/documents/supported-tunnels
- https://cloud.google.com/blog/topics/threat-intelligence/unc3944-targets-saas-applications

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_localtonet_tunnel.yml)
