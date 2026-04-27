---
sigma_id: "49a268a4-72f4-4e38-8a7b-885be690c5b5"
title: "User Added To Privilege Role"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_add.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_add.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "49a268a4-72f4-4e38-8a7b-885be690c5b5"
  - "User Added To Privilege Role"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user is added to a privileged role.

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  properties.message:
  - Add eligible member (permanent)
  - Add eligible member (eligible)
condition: selection
```

## False Positives

- Legtimate administrator actions of adding members from a role

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-identity-management#azure-ad-roles-assignment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_add.yml)
