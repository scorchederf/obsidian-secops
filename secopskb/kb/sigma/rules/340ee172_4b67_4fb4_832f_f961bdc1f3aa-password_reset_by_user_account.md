---
sigma_id: "340ee172-4b67-4fb4-832f-f961bdc1f3aa"
title: "Password Reset By User Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_user_password_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_user_password_change.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "340ee172-4b67-4fb4-832f-f961bdc1f3aa"
  - "Password Reset By User Account"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Reset By User Account

Detect when a user has reset their password in Azure AD

## Metadata

- Rule ID: 340ee172-4b67-4fb4-832f-f961bdc1f3aa
- Status: test
- Level: medium
- Author: YochanaHenderson, '@Yochana-H'
- Date: 2022-08-03
- Source Path: rules/cloud/azure/audit_logs/azure_user_password_change.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  Category: UserManagement
  Status: Success
  Initiatedby: UPN
filter:
  Target|contains: UPN
  ActivityType|contains: Password reset
condition: selection and filter
```

## False Positives

- If this was approved by System Administrator or confirmed user action.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_user_password_change.yml)
