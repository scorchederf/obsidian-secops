---
sigma_id: "413d4a81-6c98-4479-9863-014785fd579c"
title: "Okta Admin Role Assigned to an User or Group"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_admin_role_assigned_to_user_or_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_role_assigned_to_user_or_group.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "413d4a81-6c98-4479-9863-014785fd579c"
  - "Okta Admin Role Assigned to an User or Group"
attack_technique_ids:
  - "T1098.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Admin Role Assigned to an User or Group

Detects when an the Administrator role is assigned to an user or group.

## Metadata

- Rule ID: 413d4a81-6c98-4479-9863-014785fd579c
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_admin_role_assigned_to_user_or_group.yml

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Detection

```yaml
selection:
  eventtype:
  - group.privilege.grant
  - user.account.privilege.grant
condition: selection
```

## False Positives

- Administrator roles could be assigned to users or group by other admin users.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_role_assigned_to_user_or_group.yml)
