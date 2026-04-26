---
sigma_id: "542b9912-c01f-4e3f-89a8-014c48cdca7d"
title: "Azure Device No Longer Managed or Compliant"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_device_no_longer_managed_or_compliant.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_device_no_longer_managed_or_compliant.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "542b9912-c01f-4e3f-89a8-014c48cdca7d"
  - "Azure Device No Longer Managed or Compliant"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Device No Longer Managed or Compliant

Identifies when a device in azure is no longer managed or compliant

## Metadata

- Rule ID: 542b9912-c01f-4e3f-89a8-014c48cdca7d
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-03
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_device_no_longer_managed_or_compliant.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  properties.message:
  - Device no longer compliant
  - Device no longer managed
condition: selection
```

## False Positives

- Administrator may have forgotten to review the device.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#core-directory

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_device_no_longer_managed_or_compliant.yml)
