---
sigma_id: "2975af79-28c4-4d2f-a951-9095f229df29"
title: "Cobalt Strike DNS Beaconing"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_mal_cobaltstrike.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_mal_cobaltstrike.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "critical"
logsource: "dns"
aliases:
  - "2975af79-28c4-4d2f-a951-9095f229df29"
  - "Cobalt Strike DNS Beaconing"
attack_technique_ids:
  - "T1071.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious DNS queries known from Cobalt Strike beacons

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]

## Detection

```yaml
selection1:
  query|startswith:
  - aaa.stage.
  - post.1
selection2:
  query|contains: .stage.123456.
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://www.icebrg.io/blog/footprints-of-fin7-tracking-actor-patterns
- https://www.sekoia.io/en/hunting-and-detecting-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_mal_cobaltstrike.yml)
