---
sigma_id: "a0b38b70-3cb5-484b-a4eb-c4d8e7bcc0a9"
title: "Okta New Admin Console Behaviours"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_new_behaviours_admin_console.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_new_behaviours_admin_console.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "okta / okta"
aliases:
  - "a0b38b70-3cb5-484b-a4eb-c4d8e7bcc0a9"
  - "Okta New Admin Console Behaviours"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when Okta identifies new activity in the Admin Console.

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection_event:
  eventtype: policy.evaluate_sign_on
  target.displayname: Okta Admin Console
selection_positive:
- debugcontext.debugdata.behaviors|contains: POSITIVE
- debugcontext.debugdata.logonlysecuritydata|contains: POSITIVE
condition: all of selection_*
```

## False Positives

- When an admin begins using the Admin Console and one of Okta's heuristics incorrectly identifies the behavior as being unusual.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_new_behaviours_admin_console.yml)
