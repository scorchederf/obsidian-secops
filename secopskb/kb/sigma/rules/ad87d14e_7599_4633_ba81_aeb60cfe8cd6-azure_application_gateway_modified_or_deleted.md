---
sigma_id: "ad87d14e-7599-4633-ba81-aeb60cfe8cd6"
title: "Azure Application Gateway Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_application_gateway_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_application_gateway_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "ad87d14e-7599-4633-ba81-aeb60cfe8cd6"
  - "Azure Application Gateway Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Application Gateway Modified or Deleted

Identifies when a application gateway is modified or deleted.

## Metadata

- Rule ID: ad87d14e-7599-4633-ba81-aeb60cfe8cd6
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-16
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_application_gateway_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/APPLICATIONGATEWAYS/WRITE
  - MICROSOFT.NETWORK/APPLICATIONGATEWAYS/DELETE
condition: selection
```

## False Positives

- Application gateway being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Application gateway modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_application_gateway_modified_or_deleted.yml)
