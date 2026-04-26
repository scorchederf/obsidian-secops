---
sigma_id: "410d2a41-1e6d-452f-85e5-abdd8257a823"
title: "Azure Application Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_application_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_application_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "410d2a41-1e6d-452f-85e5-abdd8257a823"
  - "Azure Application Deleted"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Application Deleted

Identifies when a application is deleted in Azure.

## Metadata

- Rule ID: 410d2a41-1e6d-452f-85e5-abdd8257a823
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-03
- Modified: 2022-10-09
- Source Path: rules/cloud/azure/activity_logs/azure_application_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection:
  properties.message:
  - Delete application
  - Hard Delete application
condition: selection
```

## False Positives

- Application being deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Application deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#application-proxy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_application_deleted.yml)
