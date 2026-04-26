---
sigma_id: "9e02c8ec-02b9-43e8-81eb-34a475ba7965"
title: "Network Connection Initiated To BTunnels Domains"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_btunnels.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_btunnels.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "9e02c8ec-02b9-43e8-81eb-34a475ba7965"
  - "Network Connection Initiated To BTunnels Domains"
attack_technique_ids:
  - "T1567"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To BTunnels Domains

Detects network connections to BTunnels domains initiated by a process on the system.
Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: 9e02c8ec-02b9-43e8-81eb-34a475ba7965
- Status: test
- Level: medium
- Author: Kamran Saifullah
- Date: 2024-09-13
- Source Path: rules/windows/network_connection/net_connection_win_domain_btunnels.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith: .btunnel.co.in
condition: selection
```

## False Positives

- Legitimate use of BTunnels will also trigger this.

## References

- https://defr0ggy.github.io/research/Utilizing-BTunnel-For-Data-Exfiltration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_btunnels.yml)
