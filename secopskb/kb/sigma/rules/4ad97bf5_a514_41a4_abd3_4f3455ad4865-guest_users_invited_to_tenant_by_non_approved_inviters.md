---
sigma_id: "4ad97bf5-a514-41a4-abd3-4f3455ad4865"
title: "Guest Users Invited To Tenant By Non Approved Inviters"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_guest_users_invited_to_tenant_by_non_approved_inviters.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_guest_users_invited_to_tenant_by_non_approved_inviters.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "4ad97bf5-a514-41a4-abd3-4f3455ad4865"
  - "Guest Users Invited To Tenant By Non Approved Inviters"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Guest Users Invited To Tenant By Non Approved Inviters

Detects guest users being invited to tenant by non-approved inviters

## Metadata

- Rule ID: 4ad97bf5-a514-41a4-abd3-4f3455ad4865
- Status: test
- Level: medium
- Author: MikeDuddington, '@dudders1'
- Date: 2022-07-28
- Source Path: rules/cloud/azure/audit_logs/azure_ad_guest_users_invited_to_tenant_by_non_approved_inviters.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Category: UserManagement
  OperationName: Invite external user
filter:
  InitiatedBy|contains: <approved guest inviter use OR for multiple>
condition: selection and not filter
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts#monitoring-external-user-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_guest_users_invited_to_tenant_by_non_approved_inviters.yml)
