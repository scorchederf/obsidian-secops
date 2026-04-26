---
sigma_id: "46530378-f9db-4af9-a9e5-889c177d3881"
title: "Azure Device or Configuration Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_device_or_configuration_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_device_or_configuration_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "46530378-f9db-4af9-a9e5-889c177d3881"
  - "Azure Device or Configuration Modified or Deleted"
attack_technique_ids:
  - "T1485"
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Device or Configuration Modified or Deleted

Identifies when a device or device configuration in azure is modified or deleted.

## Metadata

- Rule ID: 46530378-f9db-4af9-a9e5-889c177d3881
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-03
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_device_or_configuration_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]
- [[kb/attack/techniques/T1565-data_manipulation|T1565.001]]

## Detection

```yaml
selection:
  properties.message:
  - Delete device
  - Delete device configuration
  - Update device
  - Update device configuration
condition: selection
```

## False Positives

- Device or device configuration being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Device or device configuration modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#core-directory

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_device_or_configuration_modified_or_deleted.yml)
