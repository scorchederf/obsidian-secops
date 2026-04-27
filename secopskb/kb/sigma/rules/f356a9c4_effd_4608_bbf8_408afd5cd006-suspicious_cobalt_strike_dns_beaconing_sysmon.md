---
sigma_id: "f356a9c4-effd-4608-bbf8-408afd5cd006"
title: "Suspicious Cobalt Strike DNS Beaconing - Sysmon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_mal_cobaltstrike.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_mal_cobaltstrike.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "critical"
logsource: "windows / dns_query"
aliases:
  - "f356a9c4-effd-4608-bbf8-408afd5cd006"
  - "Suspicious Cobalt Strike DNS Beaconing - Sysmon"
attack_technique_ids:
  - "T1071.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a program that invoked suspicious DNS queries known from Cobalt Strike beacons

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]

## Detection

```yaml
selection1:
  QueryName|startswith:
  - aaa.stage.
  - post.1
selection2:
  QueryName|contains: .stage.123456.
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://www.icebrg.io/blog/footprints-of-fin7-tracking-actor-patterns
- https://www.sekoia.io/en/hunting-and-detecting-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_mal_cobaltstrike.yml)
