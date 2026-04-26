---
sigma_id: "ca9bf243-465e-494a-9e54-bf9fc239057d"
title: "Azure Subscription Permission Elevation Via AuditLogs"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_subscription_permissions_elevation_via_auditlogs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_subscription_permissions_elevation_via_auditlogs.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "ca9bf243-465e-494a-9e54-bf9fc239057d"
  - "Azure Subscription Permission Elevation Via AuditLogs"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure Subscription Permission Elevation Via AuditLogs

Detects when a user has been elevated to manage all Azure Subscriptions.
This change should be investigated immediately if it isn't planned.
This setting could allow an attacker access to Azure subscriptions in your environment.

## Metadata

- Rule ID: ca9bf243-465e-494a-9e54-bf9fc239057d
- Status: test
- Level: high
- Author: Austin Songer @austinsonger
- Date: 2021-11-26
- Modified: 2022-12-25
- Source Path: rules/cloud/azure/audit_logs/azure_subscription_permissions_elevation_via_auditlogs.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Category: Administrative
  OperationName: Assigns the caller to user access admin
condition: selection
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts#assignment-and-elevation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_subscription_permissions_elevation_via_auditlogs.yml)
