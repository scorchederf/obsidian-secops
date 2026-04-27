---
sigma_id: "c1d147ae-a951-48e5-8b41-dcd0170c7213"
title: "App Granted Microsoft Permissions"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_permissions_msft.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_permissions_msft.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "c1d147ae-a951-48e5-8b41-dcd0170c7213"
  - "App Granted Microsoft Permissions"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# App Granted Microsoft Permissions

Detects when an application is granted delegated or app role permissions for Microsoft Graph, Exchange, Sharepoint, or Azure AD

## Metadata

- Rule ID: c1d147ae-a951-48e5-8b41-dcd0170c7213
- Status: test
- Level: high
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-10
- Source Path: rules/cloud/azure/audit_logs/azure_app_permissions_msft.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  properties.message:
  - Add delegated permission grant
  - Add app role assignment to service principal
condition: selection
```

## False Positives

- When the permission is legitimately needed for the app

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-granted-highly-privileged-permissions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_permissions_msft.yml)
