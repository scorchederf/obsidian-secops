---
sigma_id: "92cc3e5d-eb57-419d-8c16-5c63f325a401"
title: "Azure Suppression Rule Created"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_suppression_rule_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_suppression_rule_created.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "92cc3e5d-eb57-419d-8c16-5c63f325a401"
  - "Azure Suppression Rule Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Suppression Rule Created

Identifies when a suppression rule is created in Azure. Adversary's could attempt this to evade detection.

## Metadata

- Rule ID: 92cc3e5d-eb57-419d-8c16-5c63f325a401
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-16
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_suppression_rule_created.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName: MICROSOFT.SECURITY/ALERTSSUPPRESSIONRULES/WRITE
condition: selection
```

## False Positives

- Suppression Rule being created may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Suppression Rule created from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_suppression_rule_created.yml)
