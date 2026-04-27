---
sigma_id: "1d08ac94-400d-4469-a82f-daee9a908849"
title: "Communication To Ngrok Tunneling Service Initiated"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_ngrok_tunnel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_ngrok_tunnel.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "1d08ac94-400d-4469-a82f-daee9a908849"
  - "Communication To Ngrok Tunneling Service Initiated"
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

Detects an executable initiating a network connection to "ngrok" tunneling domains.
Attackers were seen using this "ngrok" in order to store their second stage payloads and malware.
While communication with such domains can be legitimate, often times is a sign of either data exfiltration by malicious actors or additional download.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[kb/attack/techniques/T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[kb/attack/techniques/T1090-proxy|T1090: Proxy]]
- [[kb/attack/techniques/T1102-web_service|T1102: Web Service]]

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

- Legitimate use of the ngrok service.

## References

- https://twitter.com/hakluke/status/1587733971814977537/photo/1
- https://ngrok.com/docs/secure-tunnels/tunnels/ssh-reverse-tunnel-agent

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_ngrok_tunnel.yml)
