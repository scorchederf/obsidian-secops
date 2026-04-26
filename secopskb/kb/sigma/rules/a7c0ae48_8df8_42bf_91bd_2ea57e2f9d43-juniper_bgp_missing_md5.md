---
sigma_id: "a7c0ae48-8df8-42bf-91bd-2ea57e2f9d43"
title: "Juniper BGP Missing MD5"
framework: "sigma"
generated: "true"
source_path: "rules/network/juniper/bgp/juniper_bgp_missing_md5.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/juniper/bgp/juniper_bgp_missing_md5.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "juniper / bgp"
aliases:
  - "a7c0ae48-8df8-42bf-91bd-2ea57e2f9d43"
  - "Juniper BGP Missing MD5"
attack_technique_ids:
  - "T1078"
  - "T1110"
  - "T1557"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Juniper BGP Missing MD5

Detects juniper BGP missing MD5 digest. Which may be indicative of brute force attacks to manipulate routing.

## Metadata

- Rule ID: a7c0ae48-8df8-42bf-91bd-2ea57e2f9d43
- Status: test
- Level: low
- Author: Tim Brown
- Date: 2023-01-09
- Modified: 2023-01-23
- Source Path: rules/network/juniper/bgp/juniper_bgp_missing_md5.yml

## Logsource

- definition: Requirements: juniper bgp logs need to be enabled and ingested
- product: juniper
- service: bgp

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]

## Detection

```yaml
keywords_bgp_juniper:
  '|all':
  - :179
  - missing MD5 digest
condition: keywords_bgp_juniper
```

## False Positives

- Unlikely. Except due to misconfigurations

## References

- https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-convery-franz-v3.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/juniper/bgp/juniper_bgp_missing_md5.yml)
