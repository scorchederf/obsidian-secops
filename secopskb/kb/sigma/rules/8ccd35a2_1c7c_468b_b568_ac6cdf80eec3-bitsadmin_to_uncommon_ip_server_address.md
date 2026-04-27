---
sigma_id: "8ccd35a2-1c7c-468b-b568-ac6cdf80eec3"
title: "Bitsadmin to Uncommon IP Server Address"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_bitsadmin_susp_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_ip.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "8ccd35a2-1c7c-468b-b568-ac6cdf80eec3"
  - "Bitsadmin to Uncommon IP Server Address"
attack_technique_ids:
  - "T1071.001"
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bitsadmin to Uncommon IP Server Address

Detects Bitsadmin connections to IP addresses instead of FQDN names

## Metadata

- Rule ID: 8ccd35a2-1c7c-468b-b568-ac6cdf80eec3
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-10
- Modified: 2022-08-24
- Source Path: rules/web/proxy_generic/proxy_ua_bitsadmin_susp_ip.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

### Software Tags

- S0190

## Detection

```yaml
selection:
  c-useragent|startswith: Microsoft BITS/
  cs-host|endswith:
  - '1'
  - '2'
  - '3'
  - '4'
  - '5'
  - '6'
  - '7'
  - '8'
  - '9'
condition: selection
```

## False Positives

- Unknown

## References

- https://isc.sans.edu/diary/Microsoft+BITS+Used+to+Download+Payloads/21027

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_ip.yml)
