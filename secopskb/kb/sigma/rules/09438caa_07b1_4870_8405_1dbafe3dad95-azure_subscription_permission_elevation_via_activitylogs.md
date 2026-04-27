---
sigma_id: "09438caa-07b1-4870-8405-1dbafe3dad95"
title: "Azure Subscription Permission Elevation Via ActivityLogs"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / activitylogs"
aliases:
  - "09438caa-07b1-4870-8405-1dbafe3dad95"
  - "Azure Subscription Permission Elevation Via ActivityLogs"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user has been elevated to manage all Azure Subscriptions.
This change should be investigated immediately if it isn't planned.
This setting could allow an attacker access to Azure subscriptions in your environment.

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  operationName: MICROSOFT.AUTHORIZATION/ELEVATEACCESS/ACTION
condition: selection
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftauthorization

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml)
