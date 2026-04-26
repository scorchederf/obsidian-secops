---
sigma_id: "0ddcff6d-d262-40b0-804b-80eb592de8e3"
title: "Azure Service Principal Created"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_service_principal_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_service_principal_created.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "0ddcff6d-d262-40b0-804b-80eb592de8e3"
  - "Azure Service Principal Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Service Principal Created

Identifies when a service principal is created in Azure.

## Metadata

- Rule ID: 0ddcff6d-d262-40b0-804b-80eb592de8e3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-02
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_service_principal_created.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  properties.message: Add service principal
condition: selection
```

## False Positives

- Service principal being created may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Service principal created from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#application-proxy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_service_principal_created.yml)
