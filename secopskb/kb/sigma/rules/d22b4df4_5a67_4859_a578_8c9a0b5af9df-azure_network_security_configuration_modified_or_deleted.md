---
sigma_id: "d22b4df4-5a67-4859-a578-8c9a0b5af9df"
title: "Azure Network Security Configuration Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_network_security_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_security_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "d22b4df4-5a67-4859-a578-8c9a0b5af9df"
  - "Azure Network Security Configuration Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Network Security Configuration Modified or Deleted

Identifies when a network security configuration is modified or deleted.

## Metadata

- Rule ID: d22b4df4-5a67-4859-a578-8c9a0b5af9df
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_network_security_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/WRITE
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/DELETE
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/WRITE
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/SECURITYRULES/DELETE
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/JOIN/ACTION
  - MICROSOFT.NETWORK/NETWORKSECURITYGROUPS/PROVIDERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE
condition: selection
```

## False Positives

- Network Security Configuration being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Network Security Configuration modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_security_modified_or_deleted.yml)
