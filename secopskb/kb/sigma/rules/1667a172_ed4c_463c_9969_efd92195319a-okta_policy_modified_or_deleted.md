---
sigma_id: "1667a172-ed4c-463c-9969-efd92195319a"
title: "Okta Policy Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_policy_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_policy_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "okta / okta"
aliases:
  - "1667a172-ed4c-463c-9969-efd92195319a"
  - "Okta Policy Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Policy Modified or Deleted

Detects when an Okta policy is modified or deleted.

## Metadata

- Rule ID: 1667a172-ed4c-463c-9969-efd92195319a
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_policy_modified_or_deleted.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype:
  - policy.lifecycle.update
  - policy.lifecycle.delete
condition: selection
```

## False Positives

- Okta Policies being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Okta Policies modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_policy_modified_or_deleted.yml)
