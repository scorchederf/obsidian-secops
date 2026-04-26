---
sigma_id: "448fd1ea-2116-4c62-9cde-a92d120e0f08"
title: "Azure Service Principal Removed"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_service_principal_removed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_service_principal_removed.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "448fd1ea-2116-4c62-9cde-a92d120e0f08"
  - "Azure Service Principal Removed"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Service Principal Removed

Identifies when a service principal was removed in Azure.

## Metadata

- Rule ID: 448fd1ea-2116-4c62-9cde-a92d120e0f08
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-03
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_service_principal_removed.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  properties.message: Remove service principal
condition: selection
```

## False Positives

- Service principal being removed may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Service principal removed from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#application-proxy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_service_principal_removed.yml)
