---
sigma_id: "a1d9eec5-33b2-4177-8d24-27fe754d0812"
title: "Cloudflared Tunnels Related DNS Requests"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_cloudflared_communication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_cloudflared_communication.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "a1d9eec5-33b2-4177-8d24-27fe754d0812"
  - "Cloudflared Tunnels Related DNS Requests"
attack_technique_ids:
  - "T1071.001"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cloudflared Tunnels Related DNS Requests

Detects DNS requests to Cloudflared tunnels domains.
Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: a1d9eec5-33b2-4177-8d24-27fe754d0812
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-12-20
- Source Path: rules/windows/dns_query/dns_query_win_cloudflared_communication.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  QueryName|endswith:
  - .v2.argotunnel.com
  - protocol-v2.argotunnel.com
  - trycloudflare.com
  - update.argotunnel.com
condition: selection
```

## False Positives

- Legitimate use of cloudflare tunnels will also trigger this.

## References

- https://www.guidepointsecurity.com/blog/tunnel-vision-cloudflared-abused-in-the-wild/
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_cloudflared_communication.yml)
