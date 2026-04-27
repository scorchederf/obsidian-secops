---
sigma_id: "11c767ae-500b-423b-bae3-b234450736ed"
title: "Users Added to Global or Device Admin Roles"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_users_added_to_device_admin_roles.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_users_added_to_device_admin_roles.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "11c767ae-500b-423b-bae3-b234450736ed"
  - "Users Added to Global or Device Admin Roles"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Monitor and alert for users added to device admin roles.

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  Category: RoleManagement
  OperationName|contains|all:
  - Add
  - member to role
  TargetResources|contains:
  - 7698a772-787b-4ac8-901f-60d6b08affd2
  - 62e90394-69f5-4237-9190-012177145e10
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#device-administrator-roles

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_users_added_to_device_admin_roles.yml)
