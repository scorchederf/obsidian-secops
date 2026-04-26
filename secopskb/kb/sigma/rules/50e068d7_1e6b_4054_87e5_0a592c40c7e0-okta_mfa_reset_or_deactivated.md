---
sigma_id: "50e068d7-1e6b-4054-87e5-0a592c40c7e0"
title: "Okta MFA Reset or Deactivated"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_mfa_reset_or_deactivated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_mfa_reset_or_deactivated.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "50e068d7-1e6b-4054-87e5-0a592c40c7e0"
  - "Okta MFA Reset or Deactivated"
attack_technique_ids:
  - "T1556.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta MFA Reset or Deactivated

Detects when an attempt at deactivating  or resetting MFA.

## Metadata

- Rule ID: 50e068d7-1e6b-4054-87e5-0a592c40c7e0
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-21
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_mfa_reset_or_deactivated.yml

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.006]]

## Detection

```yaml
selection:
  eventtype:
  - user.mfa.factor.deactivate
  - user.mfa.factor.reset_all
condition: selection
```

## False Positives

- If a MFA reset or deactivated was performed by a system administrator.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_mfa_reset_or_deactivated.yml)
