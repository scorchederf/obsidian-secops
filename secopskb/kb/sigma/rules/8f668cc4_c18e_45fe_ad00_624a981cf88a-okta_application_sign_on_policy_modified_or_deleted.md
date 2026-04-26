---
sigma_id: "8f668cc4-c18e-45fe-ad00-624a981cf88a"
title: "Okta Application Sign-On Policy Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_application_sign_on_policy_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_application_sign_on_policy_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "8f668cc4-c18e-45fe-ad00-624a981cf88a"
  - "Okta Application Sign-On Policy Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Application Sign-On Policy Modified or Deleted

Detects when an application Sign-on Policy is modified or deleted.

## Metadata

- Rule ID: 8f668cc4-c18e-45fe-ad00-624a981cf88a
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_application_sign_on_policy_modified_or_deleted.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype:
  - application.policy.sign_on.update
  - application.policy.sign_on.rule.delete
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_application_sign_on_policy_modified_or_deleted.yml)
