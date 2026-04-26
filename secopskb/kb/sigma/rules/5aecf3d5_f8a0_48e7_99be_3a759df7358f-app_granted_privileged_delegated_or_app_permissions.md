---
sigma_id: "5aecf3d5-f8a0-48e7-99be-3a759df7358f"
title: "App Granted Privileged Delegated Or App Permissions"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_privileged_permissions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_privileged_permissions.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "5aecf3d5-f8a0-48e7-99be-3a759df7358f"
  - "App Granted Privileged Delegated Or App Permissions"
attack_technique_ids:
  - "T1098.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# App Granted Privileged Delegated Or App Permissions

Detects when administrator grants either application permissions (app roles) or highly privileged delegated permissions

## Metadata

- Rule ID: 5aecf3d5-f8a0-48e7-99be-3a759df7358f
- Status: test
- Level: high
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-28
- Modified: 2023-03-29
- Source Path: rules/cloud/azure/audit_logs/azure_app_privileged_permissions.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Detection

```yaml
selection:
  properties.message: Add app role assignment to service principal
condition: selection
```

## False Positives

- When the permission is legitimately needed for the app

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-granted-highly-privileged-permissions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_privileged_permissions.yml)
