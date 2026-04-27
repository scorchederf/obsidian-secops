---
sigma_id: "91b76b84-8589-47aa-9605-c837583b82a9"
title: "Potential Okta Password in AlternateID Field"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_password_in_alternateid_field.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_password_in_alternateid_field.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "okta / okta"
aliases:
  - "91b76b84-8589-47aa-9605-c837583b82a9"
  - "Potential Okta Password in AlternateID Field"
attack_technique_ids:
  - "T1552"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user has potentially entered their password into the
username field, which will cause the password to be retained in log files.

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552: Unsecured Credentials]]

## Detection

```yaml
selection:
  legacyeventtype: core.user_auth.login_failed
filter_main:
  actor.alternateid|re: (^0oa.*|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,10})
condition: selection and not filter_main
```

## False Positives

- Unlikely

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://www.mitiga.io/blog/how-okta-passwords-can-be-compromised-uncovering-a-risk-to-user-data
- https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-create-character-restriction.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_password_in_alternateid_field.yml)
