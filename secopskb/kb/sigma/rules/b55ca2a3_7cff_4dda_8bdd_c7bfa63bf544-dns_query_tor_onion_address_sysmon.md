---
sigma_id: "b55ca2a3-7cff-4dda-8bdd-c7bfa63bf544"
title: "DNS Query Tor .Onion Address - Sysmon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_tor_onion_domain_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_tor_onion_domain_query.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / dns_query"
aliases:
  - "b55ca2a3-7cff-4dda-8bdd-c7bfa63bf544"
  - "DNS Query Tor .Onion Address - Sysmon"
attack_technique_ids:
  - "T1090.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query Tor .Onion Address - Sysmon

Detects DNS queries to an ".onion" address related to Tor routing networks

## Metadata

- Rule ID: b55ca2a3-7cff-4dda-8bdd-c7bfa63bf544
- Status: test
- Level: high
- Author: frack113
- Date: 2022-02-20
- Modified: 2025-09-12
- Source Path: rules/windows/dns_query/dns_query_win_tor_onion_domain_query.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.003]]

## Detection

```yaml
selection:
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
  - .onion.ink
  - .onion.it
  - .onion.link
  - .onion.lt
  - .onion.lu
  - .onion.nu
  - .onion.pet
  - .onion.plus
  - .onion.rip
  - .onion.sh
  - .onion.to
  - .onion.top
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

- Unknown

## References

- https://www.logpoint.com/en/blog/detecting-tor-use-with-logpoint/
- https://github.com/Azure/Azure-Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/ASimDNS/imDNS_TorProxies.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_tor_onion_domain_query.yml)
