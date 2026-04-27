---
sigma_id: "bde30855-5c53-4c18-ae90-1ff79ebc9578"
title: "Okta User Session Start Via An Anonymising Proxy Service"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_user_session_start_via_anonymised_proxy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_session_start_via_anonymised_proxy.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "okta / okta"
aliases:
  - "bde30855-5c53-4c18-ae90-1ff79ebc9578"
  - "Okta User Session Start Via An Anonymising Proxy Service"
attack_technique_ids:
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when an Okta user session starts where the user is behind an anonymising proxy service.

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Detection

```yaml
selection:
  eventtype: user.session.start
  securitycontext.isproxy: 'true'
condition: selection
```

## False Positives

- If a user requires an anonymising proxy due to valid justifications.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_session_start_via_anonymised_proxy.yml)
