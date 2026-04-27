---
sigma_id: "c4568f5d-131f-4e78-83d4-45b2da0ec4f1"
title: "Communication To LocaltoNet Tunneling Service Initiated - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/network_connection/net_connection_lnx_domain_localtonet_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_domain_localtonet_tunnel.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "linux / network_connection"
aliases:
  - "c4568f5d-131f-4e78-83d4-45b2da0ec4f1"
  - "Communication To LocaltoNet Tunneling Service Initiated - Linux"
attack_technique_ids:
  - "T1572"
  - "T1090"
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects an executable initiating a network connection to "LocaltoNet" tunneling sub-domains.
LocaltoNet is a reverse proxy that enables localhost services to be exposed to the Internet.
Attackers have been seen to use this service for command-and-control activities to bypass MFA and perimeter controls.

## Logsource

- category: network_connection
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[kb/attack/techniques/T1090-proxy|T1090: Proxy]]
- [[kb/attack/techniques/T1102-web_service|T1102: Web Service]]

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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_domain_localtonet_tunnel.yml)
