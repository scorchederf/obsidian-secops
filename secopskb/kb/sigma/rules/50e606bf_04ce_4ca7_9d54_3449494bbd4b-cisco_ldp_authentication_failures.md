---
sigma_id: "50e606bf-04ce-4ca7-9d54-3449494bbd4b"
title: "Cisco LDP Authentication Failures"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/ldp/cisco_ldp_md5_auth_failed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/ldp/cisco_ldp_md5_auth_failed.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "cisco / ldp"
aliases:
  - "50e606bf-04ce-4ca7-9d54-3449494bbd4b"
  - "Cisco LDP Authentication Failures"
attack_technique_ids:
  - "T1078"
  - "T1110"
  - "T1557"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco LDP Authentication Failures

Detects LDP failures which may be indicative of brute force attacks to manipulate MPLS labels

## Metadata

- Rule ID: 50e606bf-04ce-4ca7-9d54-3449494bbd4b
- Status: test
- Level: low
- Author: Tim Brown
- Date: 2023-01-09
- Source Path: rules/network/cisco/ldp/cisco_ldp_md5_auth_failed.yml

## Logsource

- definition: Requirements: cisco ldp logs need to be enabled and ingested
- product: cisco
- service: ldp

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]

## Detection

```yaml
selection_protocol:
- LDP
selection_keywords:
- SOCKET_TCP_PACKET_MD5_AUTHEN_FAIL
- TCPMD5AuthenFail
condition: selection_protocol and selection_keywords
```

## False Positives

- Unlikely. Except due to misconfigurations

## References

- https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-convery-franz-v3.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/ldp/cisco_ldp_md5_auth_failed.yml)
