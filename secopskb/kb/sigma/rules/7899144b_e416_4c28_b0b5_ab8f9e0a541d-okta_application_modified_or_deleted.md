---
sigma_id: "7899144b-e416-4c28-b0b5-ab8f9e0a541d"
title: "Okta Application Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_application_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_application_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "7899144b-e416-4c28-b0b5-ab8f9e0a541d"
  - "Okta Application Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Application Modified or Deleted

Detects when an application is modified or deleted.

## Metadata

- Rule ID: 7899144b-e416-4c28-b0b5-ab8f9e0a541d
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_application_modified_or_deleted.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype:
  - application.lifecycle.update
  - application.lifecycle.delete
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_application_modified_or_deleted.yml)
