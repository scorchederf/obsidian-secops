---
sigma_id: "0255a820-e564-4e40-af2b-6ac61160335c"
title: "A New Trust Was Created To A Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_add_domain_trust.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_add_domain_trust.yml"
build_date: "2026-04-26 14:14:19"
status: "stable"
level: "medium"
logsource: "windows / security"
aliases:
  - "0255a820-e564-4e40-af2b-6ac61160335c"
  - "A New Trust Was Created To A Domain"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# A New Trust Was Created To A Domain

Addition of domains is seldom and should be verified for legitimacy.

## Metadata

- Rule ID: 0255a820-e564-4e40-af2b-6ac61160335c
- Status: stable
- Level: medium
- Author: Thomas Patzke
- Date: 2019-12-03
- Modified: 2024-01-16
- Source Path: rules/windows/builtin/security/win_security_susp_add_domain_trust.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  EventID: 4706
condition: selection
```

## False Positives

- Legitimate extension of domain structure

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4706

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_add_domain_trust.yml)
