---
sigma_id: "56fa3cd6-f8d6-4520-a8c7-607292971886"
title: "Cisco BGP Authentication Failures"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/bgp/cisco_bgp_md5_auth_failed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/bgp/cisco_bgp_md5_auth_failed.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "cisco / bgp"
aliases:
  - "56fa3cd6-f8d6-4520-a8c7-607292971886"
  - "Cisco BGP Authentication Failures"
attack_technique_ids:
  - "T1078"
  - "T1110"
  - "T1557"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco BGP Authentication Failures

Detects BGP failures which may be indicative of brute force attacks to manipulate routing

## Metadata

- Rule ID: 56fa3cd6-f8d6-4520-a8c7-607292971886
- Status: test
- Level: low
- Author: Tim Brown
- Date: 2023-01-09
- Modified: 2023-01-23
- Source Path: rules/network/cisco/bgp/cisco_bgp_md5_auth_failed.yml

## Logsource

- definition: Requirements: cisco bgp logs need to be enabled and ingested
- product: cisco
- service: bgp

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]

## Detection

```yaml
keywords_bgp_cisco:
  '|all':
  - :179
  - IP-TCP-3-BADAUTH
condition: keywords_bgp_cisco
```

## False Positives

- Unlikely. Except due to misconfigurations

## References

- https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-convery-franz-v3.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/bgp/cisco_bgp_md5_auth_failed.yml)
