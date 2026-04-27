---
sigma_id: "ee39a9f7-5a79-4b0a-9815-d36b3cf28d3e"
title: "Okta FastPass Phishing Detection"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_fastpass_phishing_detection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_fastpass_phishing_detection.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "okta / okta"
aliases:
  - "ee39a9f7-5a79-4b0a-9815-d36b3cf28d3e"
  - "Okta FastPass Phishing Detection"
attack_technique_ids:
  - "T1566"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when Okta FastPass prevents a known phishing site.

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566: Phishing]]

## Detection

```yaml
selection:
  outcome.reason: FastPass declined phishing attempt
  outcome.result: FAILURE
  eventtype: user.authentication.auth_via_mfa
condition: selection
```

## False Positives

- Unlikely

## References

- https://sec.okta.com/fastpassphishingdetection
- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_fastpass_phishing_detection.yml)
