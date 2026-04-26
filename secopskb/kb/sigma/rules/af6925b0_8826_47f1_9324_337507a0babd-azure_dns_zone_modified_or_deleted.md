---
sigma_id: "af6925b0-8826-47f1-9324-337507a0babd"
title: "Azure DNS Zone Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_dns_zone_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_dns_zone_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "af6925b0-8826-47f1-9324-337507a0babd"
  - "Azure DNS Zone Modified or Deleted"
attack_technique_ids:
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure DNS Zone Modified or Deleted

Identifies when DNS zone is modified or deleted.

## Metadata

- Rule ID: af6925b0-8826-47f1-9324-337507a0babd
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_dns_zone_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation|T1565.001]]

## Detection

```yaml
selection:
  operationName|startswith: MICROSOFT.NETWORK/DNSZONES
  operationName|endswith:
  - /WRITE
  - /DELETE
condition: selection
```

## False Positives

- DNS zone modified and deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- DNS zone modification from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_dns_zone_modified_or_deleted.yml)
