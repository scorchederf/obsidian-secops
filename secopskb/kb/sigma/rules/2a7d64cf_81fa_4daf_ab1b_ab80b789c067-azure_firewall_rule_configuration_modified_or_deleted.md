---
sigma_id: "2a7d64cf-81fa-4daf-ab1b-ab80b789c067"
title: "Azure Firewall Rule Configuration Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_network_firewall_rule_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_firewall_rule_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "2a7d64cf-81fa-4daf-ab1b-ab80b789c067"
  - "Azure Firewall Rule Configuration Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Firewall Rule Configuration Modified or Deleted

Identifies when a Firewall Rule Configuration is Modified or Deleted.

## Metadata

- Rule ID: 2a7d64cf-81fa-4daf-ab1b-ab80b789c067
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_network_firewall_rule_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/RULECOLLECTIONGROUPS/WRITE
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/RULECOLLECTIONGROUPS/DELETE
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/RULEGROUPS/WRITE
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/RULEGROUPS/DELETE
condition: selection
```

## False Positives

- Firewall Rule Configuration being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Firewall Rule Configuration modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_firewall_rule_modified_or_deleted.yml)
