---
sigma_id: "9501f8e6-8e3d-48fc-a8a6-1089dd5d7ef4"
title: "Network Connection Initiated To DevTunnels Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_devtunnels.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "9501f8e6-8e3d-48fc-a8a6-1089dd5d7ef4"
  - "Network Connection Initiated To DevTunnels Domain"
attack_technique_ids:
  - "T1567.001"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To DevTunnels Domain

Detects network connections to Devtunnels domains initiated by a process on a system. Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: 9501f8e6-8e3d-48fc-a8a6-1089dd5d7ef4
- Status: test
- Level: medium
- Author: Kamran Saifullah
- Date: 2023-11-20
- Source Path: rules/windows/network_connection/net_connection_win_domain_devtunnels.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.001]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith: .devtunnels.ms
condition: selection
```

## False Positives

- Legitimate use of Devtunnels will also trigger this.

## References

- https://blueteamops.medium.com/detecting-dev-tunnels-16f0994dc3e2
- https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/security
- https://cydefops.com/devtunnels-unleashed

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml)
