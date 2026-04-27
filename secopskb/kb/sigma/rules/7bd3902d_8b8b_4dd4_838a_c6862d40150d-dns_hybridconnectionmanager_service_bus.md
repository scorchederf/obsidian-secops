---
sigma_id: "7bd3902d-8b8b-4dd4-838a-c6862d40150d"
title: "DNS HybridConnectionManager Service Bus"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_hybridconnectionmgr_servicebus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_hybridconnectionmgr_servicebus.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / dns_query"
aliases:
  - "7bd3902d-8b8b-4dd4-838a-c6862d40150d"
  - "DNS HybridConnectionManager Service Bus"
attack_technique_ids:
  - "T1554"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Azure Hybrid Connection Manager services querying the Azure service bus service

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1554-compromise_host_software_binary|T1554: Compromise Host Software Binary]]

## Detection

```yaml
selection:
  QueryName|contains: servicebus.windows.net
  Image|contains: HybridConnectionManager
condition: selection
```

## False Positives

- Legitimate use of Azure Hybrid Connection Manager and the Azure Service Bus service

## References

- https://twitter.com/Cyb3rWard0g/status/1381642789369286662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_hybridconnectionmgr_servicebus.yml)
