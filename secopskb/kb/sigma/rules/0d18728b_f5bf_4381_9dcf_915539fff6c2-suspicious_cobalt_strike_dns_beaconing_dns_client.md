---
sigma_id: "0d18728b-f5bf-4381-9dcf-915539fff6c2"
title: "Suspicious Cobalt Strike DNS Beaconing - DNS Client"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_client/win_dns_client_mal_cobaltstrike.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_mal_cobaltstrike.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "critical"
logsource: "windows / dns-client"
aliases:
  - "0d18728b-f5bf-4381-9dcf-915539fff6c2"
  - "Suspicious Cobalt Strike DNS Beaconing - DNS Client"
attack_technique_ids:
  - "T1071.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a program that invoked suspicious DNS queries known from Cobalt Strike beacons

## Logsource

- definition: Requirements: Microsoft-Windows-DNS Client Events/Operational Event Log must be enabled/collected in order to receive the events.
- product: windows
- service: dns-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]

## Detection

```yaml
selection_eid:
  EventID: 3008
selection_query_1:
  QueryName|startswith:
  - aaa.stage.
  - post.1
selection_query_2:
  QueryName|contains: .stage.123456.
condition: selection_eid and 1 of selection_query_*
```

## False Positives

- Unknown

## References

- https://www.icebrg.io/blog/footprints-of-fin7-tracking-actor-patterns
- https://www.sekoia.io/en/hunting-and-detecting-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_mal_cobaltstrike.yml)
