---
sigma_id: "8384bd26-bde6-4da9-8e5d-4174a7a47ca2"
title: "Query Tor Onion Address - DNS Client"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_client/win_dns_client_tor_onion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_tor_onion.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / dns-client"
aliases:
  - "8384bd26-bde6-4da9-8e5d-4174a7a47ca2"
  - "Query Tor Onion Address - DNS Client"
attack_technique_ids:
  - "T1090.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Query Tor Onion Address - DNS Client

Detects DNS resolution of an .onion address related to Tor routing networks

## Metadata

- Rule ID: 8384bd26-bde6-4da9-8e5d-4174a7a47ca2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-02-20
- Modified: 2025-09-12
- Source Path: rules/windows/builtin/dns_client/win_dns_client_tor_onion.yml

## Logsource

- definition: Requirements: Microsoft-Windows-DNS Client Events/Operational Event Log must be enabled/collected in order to receive the events.
- product: windows
- service: dns-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.003]]

## Detection

```yaml
selection:
  EventID: 3008
  QueryName|endswith:
  - .hiddenservice.net
  - .onion.ca
  - .onion.cab
  - .onion.casa
  - .onion.city
  - .onion.direct
  - .onion.dog
  - .onion.glass
  - .onion.gq
  - .onion.guide
  - .onion.in.net
  - .onion.ink
  - .onion.it
  - .onion.link
  - .onion.lt
  - .onion.lu
  - .onion.ly
  - .onion.mn
  - .onion.network
  - .onion.nu
  - .onion.pet
  - .onion.plus
  - .onion.pt
  - .onion.pw
  - .onion.rip
  - .onion.sh
  - .onion.si
  - .onion.to
  - .onion.top
  - .onion.ws
  - .onion
  - .s1.tor-gateways.de
  - .s2.tor-gateways.de
  - .s3.tor-gateways.de
  - .s4.tor-gateways.de
  - .s5.tor-gateways.de
  - .t2w.pw
  - .tor2web.ae.org
  - .tor2web.blutmagie.de
  - .tor2web.com
  - .tor2web.fi
  - .tor2web.io
  - .tor2web.org
  - .tor2web.xyz
  - .torlink.co
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.logpoint.com/en/blog/detecting-tor-use-with-logpoint/
- https://github.com/Azure/Azure-Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/ASimDNS/imDNS_TorProxies.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_tor_onion.yml)
