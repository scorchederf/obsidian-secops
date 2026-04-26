---
sigma_id: "0c97c1d3-4057-45c9-b148-1de94b631931"
title: "Okta Policy Rule Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_policy_rule_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_policy_rule_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "0c97c1d3-4057-45c9-b148-1de94b631931"
  - "Okta Policy Rule Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Policy Rule Modified or Deleted

Detects when an Policy Rule is Modified or Deleted.

## Metadata

- Rule ID: 0c97c1d3-4057-45c9-b148-1de94b631931
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_policy_rule_modified_or_deleted.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype:
  - policy.rule.update
  - policy.rule.delete
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_policy_rule_modified_or_deleted.yml)
