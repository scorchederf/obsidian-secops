---
sigma_id: "025c9fe7-db72-49f9-af0d-31341dd7dd57"
title: "Azure Firewall Rule Collection Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_firewall_rule_collection_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_firewall_rule_collection_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "025c9fe7-db72-49f9-af0d-31341dd7dd57"
  - "Azure Firewall Rule Collection Modified or Deleted"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Firewall Rule Collection Modified or Deleted

Identifies when Rule Collections (Application, NAT, and Network) is being modified or deleted.

## Metadata

- Rule ID: 025c9fe7-db72-49f9-af0d-31341dd7dd57
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_firewall_rule_collection_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/AZUREFIREWALLS/APPLICATIONRULECOLLECTIONS/WRITE
  - MICROSOFT.NETWORK/AZUREFIREWALLS/APPLICATIONRULECOLLECTIONS/DELETE
  - MICROSOFT.NETWORK/AZUREFIREWALLS/NATRULECOLLECTIONS/WRITE
  - MICROSOFT.NETWORK/AZUREFIREWALLS/NATRULECOLLECTIONS/DELETE
  - MICROSOFT.NETWORK/AZUREFIREWALLS/NETWORKRULECOLLECTIONS/WRITE
  - MICROSOFT.NETWORK/AZUREFIREWALLS/NETWORKRULECOLLECTIONS/DELETE
condition: selection
```

## False Positives

- Rule Collections (Application, NAT, and Network) being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Rule Collections (Application, NAT, and Network) modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_firewall_rule_collection_modified_or_deleted.yml)
