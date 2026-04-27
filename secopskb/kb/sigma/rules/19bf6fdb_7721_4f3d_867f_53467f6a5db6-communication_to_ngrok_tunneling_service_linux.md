---
sigma_id: "19bf6fdb-7721-4f3d-867f-53467f6a5db6"
title: "Communication To Ngrok Tunneling Service - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/network_connection/net_connection_lnx_ngrok_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_ngrok_tunnel.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "linux / network_connection"
aliases:
  - "19bf6fdb-7721-4f3d-867f-53467f6a5db6"
  - "Communication To Ngrok Tunneling Service - Linux"
attack_technique_ids:
  - "T1567"
  - "T1568.002"
  - "T1572"
  - "T1090"
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Communication To Ngrok Tunneling Service - Linux

Detects an executable accessing an ngrok tunneling endpoint, which could be a sign of forbidden exfiltration of data exfiltration by malicious actors

## Metadata

- Rule ID: 19bf6fdb-7721-4f3d-867f-53467f6a5db6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-11-03
- Source Path: rules/linux/network_connection/net_connection_lnx_ngrok_tunnel.yml

## Logsource

- category: network_connection
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]
- [[kb/attack/techniques/T1568-dynamic_resolution|T1568.002]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1090-proxy|T1090]]
- [[kb/attack/techniques/T1102-web_service|T1102]]

### Software Tags

- S0508

## Detection

```yaml
selection:
  DestinationHostname|contains:
  - tunnel.us.ngrok.com
  - tunnel.eu.ngrok.com
  - tunnel.ap.ngrok.com
  - tunnel.au.ngrok.com
  - tunnel.sa.ngrok.com
  - tunnel.jp.ngrok.com
  - tunnel.in.ngrok.com
condition: selection
```

## False Positives

- Legitimate use of ngrok

## References

- https://twitter.com/hakluke/status/1587733971814977537/photo/1
- https://ngrok.com/docs/secure-tunnels/tunnels/ssh-reverse-tunnel-agent

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_ngrok_tunnel.yml)
