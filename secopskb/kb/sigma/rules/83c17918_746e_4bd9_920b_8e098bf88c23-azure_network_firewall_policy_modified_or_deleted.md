---
sigma_id: "83c17918-746e-4bd9-920b-8e098bf88c23"
title: "Azure Network Firewall Policy Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_network_firewall_policy_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_firewall_policy_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "83c17918-746e-4bd9-920b-8e098bf88c23"
  - "Azure Network Firewall Policy Modified or Deleted"
attack_technique_ids:
  - "T1562.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Network Firewall Policy Modified or Deleted

Identifies when a Firewall Policy is Modified or Deleted.

## Metadata

- Rule ID: 83c17918-746e-4bd9-920b-8e098bf88c23
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-02
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_network_firewall_policy_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.007]]

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/WRITE
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/JOIN/ACTION
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/CERTIFICATES/ACTION
  - MICROSOFT.NETWORK/FIREWALLPOLICIES/DELETE
condition: selection
```

## False Positives

- Firewall Policy being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Firewall Policy modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_firewall_policy_modified_or_deleted.yml)
