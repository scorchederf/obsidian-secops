---
sigma_id: "a6355fbe-f36f-45d8-8efc-ab42465cbc52"
title: "Delegated Permissions Granted For All Users"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_delegated_permissions_all_users.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_delegated_permissions_all_users.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "a6355fbe-f36f-45d8-8efc-ab42465cbc52"
  - "Delegated Permissions Granted For All Users"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Delegated Permissions Granted For All Users

Detects when highly privileged delegated permissions are granted on behalf of all users

## Metadata

- Rule ID: a6355fbe-f36f-45d8-8efc-ab42465cbc52
- Status: test
- Level: high
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-28
- Source Path: rules/cloud/azure/audit_logs/azure_app_delegated_permissions_all_users.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  properties.message: Add delegated permission grant
condition: selection
```

## False Positives

- When the permission is legitimately needed for the app

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-granted-highly-privileged-permissions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_delegated_permissions_all_users.yml)
