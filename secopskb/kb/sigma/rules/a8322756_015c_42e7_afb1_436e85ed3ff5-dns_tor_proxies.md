---
sigma_id: "a8322756-015c-42e7-afb1-436e85ed3ff5"
title: "DNS TOR Proxies"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dns_torproxy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_torproxy.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "zeek / dns"
aliases:
  - "a8322756-015c-42e7-afb1-436e85ed3ff5"
  - "DNS TOR Proxies"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS TOR Proxies

Identifies IPs performing DNS lookups associated with common Tor proxies.

## Metadata

- Rule ID: a8322756-015c-42e7-afb1-436e85ed3ff5
- Status: test
- Level: medium
- Author: Saw Winn Naung , Azure-Sentinel
- Date: 2021-08-15
- Modified: 2025-09-12
- Source Path: rules/network/zeek/zeek_dns_torproxy.yml

## Logsource

- product: zeek
- service: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection:
  query|endswith:
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

- Unknown

## References

- https://github.com/Azure/Azure-Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/ASimDNS/imDNS_TorProxies.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_torproxy.yml)
