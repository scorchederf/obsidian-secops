---
sigma_id: "7cd1dcdc-6edf-4896-86dc-d1f19ad64903"
title: "Network Connection Initiated To Cloudflared Tunnels Domains"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_cloudflared_communication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_cloudflared_communication.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "7cd1dcdc-6edf-4896-86dc-d1f19ad64903"
  - "Network Connection Initiated To Cloudflared Tunnels Domains"
attack_technique_ids:
  - "T1567"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To Cloudflared Tunnels Domains

Detects network connections to Cloudflared tunnels domains initiated by a process on the system.
Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: 7cd1dcdc-6edf-4896-86dc-d1f19ad64903
- Status: test
- Level: medium
- Author: Kamran Saifullah, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-05-27
- Source Path: rules/windows/network_connection/net_connection_win_domain_cloudflared_communication.yml

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
  DestinationHostname|endswith:
  - .v2.argotunnel.com
  - protocol-v2.argotunnel.com
  - trycloudflare.com
  - update.argotunnel.com
condition: selection
```

## False Positives

- Legitimate use of cloudflare tunnels will also trigger this.

## References

- https://defr0ggy.github.io/research/Abusing-Cloudflared-A-Proxy-Service-To-Host-Share-Applications/
- https://www.guidepointsecurity.com/blog/tunnel-vision-cloudflared-abused-in-the-wild/
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_cloudflared_communication.yml)
