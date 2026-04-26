---
sigma_id: "636e30d5-3736-42ea-96b1-e6e2f8429fd6"
title: "Azure Owner Removed From Application or Service Principal"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_owner_removed_from_application_or_service_principal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_owner_removed_from_application_or_service_principal.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "636e30d5-3736-42ea-96b1-e6e2f8429fd6"
  - "Azure Owner Removed From Application or Service Principal"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Owner Removed From Application or Service Principal

Identifies when a owner is was removed from a application or service principal in Azure.

## Metadata

- Rule ID: 636e30d5-3736-42ea-96b1-e6e2f8429fd6
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-03
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_owner_removed_from_application_or_service_principal.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  properties.message:
  - Remove owner from service principal
  - Remove owner from application
condition: selection
```

## False Positives

- Owner being removed may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Owner removed from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#application-proxy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_owner_removed_from_application_or_service_principal.yml)
