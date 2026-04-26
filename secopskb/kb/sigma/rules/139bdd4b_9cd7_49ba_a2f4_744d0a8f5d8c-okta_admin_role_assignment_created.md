---
sigma_id: "139bdd4b-9cd7-49ba-a2f4-744d0a8f5d8c"
title: "Okta Admin Role Assignment Created"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_admin_role_assignment_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_role_assignment_created.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "139bdd4b-9cd7-49ba-a2f4-744d0a8f5d8c"
  - "Okta Admin Role Assignment Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Admin Role Assignment Created

Detects when a new admin role assignment is created. Which could be a sign of privilege escalation or persistence

## Metadata

- Rule ID: 139bdd4b-9cd7-49ba-a2f4-744d0a8f5d8c
- Status: test
- Level: medium
- Author: Nikita Khalimonenkov
- Date: 2023-01-19
- Source Path: rules/identity/okta/okta_admin_role_assignment_created.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype: iam.resourceset.bindings.add
condition: selection
```

## False Positives

- Legitimate creation of a new admin role assignment

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_role_assignment_created.yml)
