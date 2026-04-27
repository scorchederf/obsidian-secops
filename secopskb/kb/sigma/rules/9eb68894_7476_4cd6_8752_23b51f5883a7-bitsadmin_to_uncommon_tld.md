---
sigma_id: "9eb68894-7476-4cd6-8752-23b51f5883a7"
title: "Bitsadmin to Uncommon TLD"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "9eb68894-7476-4cd6-8752-23b51f5883a7"
  - "Bitsadmin to Uncommon TLD"
attack_technique_ids:
  - "T1071.001"
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Bitsadmin connections to domains with uncommon TLDs

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[kb/attack/techniques/T1197-bits_jobs|T1197: BITS Jobs]]

### Software Tags

- S0190

## Detection

```yaml
selection:
  c-useragent|startswith: Microsoft BITS/
falsepositives:
  cs-host|endswith:
  - .com
  - .net
  - .org
  - .scdn.co
  - .sfx.ms
condition: selection and not falsepositives
```

## False Positives

- Rare programs that use Bitsadmin and update from regional TLDs e.g. .uk or .ca

## References

- https://twitter.com/jhencinski/status/1102695118455349248
- https://isc.sans.edu/forums/diary/Investigating+Microsoft+BITS+Activity/23281/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml)
