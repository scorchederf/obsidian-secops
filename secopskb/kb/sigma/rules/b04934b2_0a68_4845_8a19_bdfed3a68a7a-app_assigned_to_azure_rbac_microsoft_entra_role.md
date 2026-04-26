---
sigma_id: "b04934b2-0a68-4845-8a19-bdfed3a68a7a"
title: "App Assigned To Azure RBAC/Microsoft Entra Role"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_role_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_role_added.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "b04934b2-0a68-4845-8a19-bdfed3a68a7a"
  - "App Assigned To Azure RBAC/Microsoft Entra Role"
attack_technique_ids:
  - "T1098.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# App Assigned To Azure RBAC/Microsoft Entra Role

Detects when an app is assigned Azure AD roles, such as global administrator, or Azure RBAC roles, such as subscription owner.

## Metadata

- Rule ID: b04934b2-0a68-4845-8a19-bdfed3a68a7a
- Status: test
- Level: medium
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-19
- Modified: 2024-11-04
- Source Path: rules/cloud/azure/audit_logs/azure_app_role_added.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Detection

```yaml
selection:
  targetResources.type: Service Principal
  properties.message:
  - Add member to role
  - Add eligible member to role
  - Add scoped member to role
condition: selection
```

## False Positives

- When the permission is legitimately needed for the app

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#service-principal-assigned-to-a-role

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_role_added.yml)
