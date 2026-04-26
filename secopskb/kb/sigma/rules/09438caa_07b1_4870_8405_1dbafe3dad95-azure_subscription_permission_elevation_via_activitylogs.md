---
sigma_id: "09438caa-07b1-4870-8405-1dbafe3dad95"
title: "Azure Subscription Permission Elevation Via ActivityLogs"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml"
build_date: "2026-04-26 15:01:43"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure Subscription Permission Elevation Via ActivityLogs

Detects when a user has been elevated to manage all Azure Subscriptions.
This change should be investigated immediately if it isn't planned.
This setting could allow an attacker access to Azure subscriptions in your environment.

## Metadata

- Rule ID: 09438caa-07b1-4870-8405-1dbafe3dad95
- Status: test
- Level: high
- Author: Austin Songer @austinsonger
- Date: 2021-11-26
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_subscription_permissions_elevation_via_activitylogs.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

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
