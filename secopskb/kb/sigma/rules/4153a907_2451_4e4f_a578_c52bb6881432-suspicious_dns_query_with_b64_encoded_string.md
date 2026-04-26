---
sigma_id: "4153a907-2451-4e4f-a578-c52bb6881432"
title: "Suspicious DNS Query with B64 Encoded String"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_susp_b64_queries.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_b64_queries.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "dns"
aliases:
  - "4153a907-2451-4e4f-a578-c52bb6881432"
  - "Suspicious DNS Query with B64 Encoded String"
attack_technique_ids:
  - "T1048.003"
  - "T1071.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious DNS Query with B64 Encoded String

Detects suspicious DNS queries using base64 encoding

## Metadata

- Rule ID: 4153a907-2451-4e4f-a578-c52bb6881432
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-05-10
- Modified: 2022-10-09
- Source Path: rules/network/dns/net_dns_susp_b64_queries.yml

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]

## Detection

```yaml
selection:
  query|contains: ==.
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/krmaxwell/dns-exfiltration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_b64_queries.yml)
