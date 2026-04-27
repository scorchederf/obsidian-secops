---
sigma_id: "07e97cc6-aed1-43ae-9081-b3470d2367f1"
title: "Okta Suspicious Activity Reported by End-user"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_suspicious_activity_enduser_report.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_suspicious_activity_enduser_report.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "okta / okta"
aliases:
  - "07e97cc6-aed1-43ae-9081-b3470d2367f1"
  - "Okta Suspicious Activity Reported by End-user"
attack_technique_ids:
  - "T1586.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when an Okta end-user reports activity by their account as being potentially suspicious.

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1586-compromise_accounts#^t1586003-cloud-accounts|T1586.003: Cloud Accounts]]

## Detection

```yaml
selection:
  eventtype: user.account.report_suspicious_activity_by_enduser
condition: selection
```

## False Positives

- If an end-user incorrectly identifies normal activity as suspicious.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://github.com/okta/workflows-templates/blob/1164f0eb71ce47c9ddc7d850e9ab87b5a2b42333/workflows/suspicious_activity_reported/readme.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_suspicious_activity_enduser_report.yml)
