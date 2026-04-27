---
sigma_id: "1f978c6a-4415-47fb-aca5-736a44d7ca3d"
title: "Cisco Crypto Commands"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_crypto_actions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_crypto_actions.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "cisco / aaa"
aliases:
  - "1f978c6a-4415-47fb-aca5-736a44d7ca3d"
  - "Cisco Crypto Commands"
attack_technique_ids:
  - "T1553.004"
  - "T1552.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cisco Crypto Commands

Show when private keys are being exported from the device, or when new certificates are installed

## Metadata

- Rule ID: 1f978c6a-4415-47fb-aca5-736a44d7ca3d
- Status: test
- Level: high
- Author: Austin Clark
- Date: 2019-08-12
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_crypto_actions.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Detection

```yaml
keywords:
- crypto pki export
- crypto pki import
- crypto pki trustpoint
condition: keywords
```

## False Positives

- Not commonly run by administrators. Also whitelist your known good certificates

## References

- https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/a1/sec-a1-cr-book/sec-a1-cr-book_chapter_0111.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_crypto_actions.yml)
