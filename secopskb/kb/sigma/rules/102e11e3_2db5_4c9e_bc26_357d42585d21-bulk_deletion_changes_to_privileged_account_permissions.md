---
sigma_id: "102e11e3-2db5-4c9e-bc26-357d42585d21"
title: "Bulk Deletion Changes To Privileged Account Permissions"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_bulk_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_bulk_change.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "102e11e3-2db5-4c9e-bc26-357d42585d21"
  - "Bulk Deletion Changes To Privileged Account Permissions"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bulk Deletion Changes To Privileged Account Permissions

Detects when a user is removed from a privileged role. Bulk changes should be investigated.

## Metadata

- Rule ID: 102e11e3-2db5-4c9e-bc26-357d42585d21
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
- Date: 2022-08-05
- Source Path: rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_bulk_change.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  properties.message:
  - Remove eligible member (permanent)
  - Remove eligible member (eligible)
condition: selection
```

## False Positives

- Legtimate administrator actions of removing members from a role

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-identity-management#azure-ad-roles-assignment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_priviledged_role_assignment_bulk_change.yml)
