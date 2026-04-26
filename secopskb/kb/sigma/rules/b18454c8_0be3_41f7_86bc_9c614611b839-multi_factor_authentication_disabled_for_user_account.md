---
sigma_id: "b18454c8-0be3-41f7-86bc-9c614611b839"
title: "Multi Factor Authentication Disabled For User Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_user_account_mfa_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_user_account_mfa_disable.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "b18454c8-0be3-41f7-86bc-9c614611b839"
  - "Multi Factor Authentication Disabled For User Account"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Multi Factor Authentication Disabled For User Account

Detects changes to the "StrongAuthenticationRequirement" value, where the state is set to "0" or "Disabled".
Threat actors were seen disabling multi factor authentication for users in order to maintain or achieve access to the account. Also see in SIM Swap attacks.

## Metadata

- Rule ID: b18454c8-0be3-41f7-86bc-9c614611b839
- Status: test
- Level: medium
- Author: Harjot Singh (@cyb3rjy0t)
- Date: 2024-08-21
- Source Path: rules/cloud/azure/audit_logs/azure_user_account_mfa_disable.yml

## Logsource

- definition: Requirements: The TargetResources array needs to be mapped accurately in order for this rule to work
- product: azure
- service: auditlogs

## Detection

```yaml
selection:
  LoggedByService: Core Directory
  Category: UserManagement
  OperationName: Update user
  TargetResources.ModifiedProperties.DisplayName: StrongAuthenticationRequirement
  TargetResources.ModifiedProperties.NewValue|contains: State":0
condition: selection
```

## False Positives

- Legitimate authorized activity.

## References

- https://www.sans.org/blog/defending-against-scattered-spider-and-the-com-with-cybercrime-intelligence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_user_account_mfa_disable.yml)
