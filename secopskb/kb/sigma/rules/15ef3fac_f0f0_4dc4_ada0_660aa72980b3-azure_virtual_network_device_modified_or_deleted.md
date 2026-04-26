---
sigma_id: "15ef3fac-f0f0-4dc4-ada0-660aa72980b3"
title: "Azure Virtual Network Device Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_network_virtual_device_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_virtual_device_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "15ef3fac-f0f0-4dc4-ada0-660aa72980b3"
  - "Azure Virtual Network Device Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Virtual Network Device Modified or Deleted

Identifies when a virtual network device is being modified or deleted.
This can be a network interface, network virtual appliance, virtual hub, or virtual router.

## Metadata

- Rule ID: 15ef3fac-f0f0-4dc4-ada0-660aa72980b3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_network_virtual_device_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/NETWORKINTERFACES/TAPCONFIGURATIONS/WRITE
  - MICROSOFT.NETWORK/NETWORKINTERFACES/TAPCONFIGURATIONS/DELETE
  - MICROSOFT.NETWORK/NETWORKINTERFACES/WRITE
  - MICROSOFT.NETWORK/NETWORKINTERFACES/JOIN/ACTION
  - MICROSOFT.NETWORK/NETWORKINTERFACES/DELETE
  - MICROSOFT.NETWORK/NETWORKVIRTUALAPPLIANCES/DELETE
  - MICROSOFT.NETWORK/NETWORKVIRTUALAPPLIANCES/WRITE
  - MICROSOFT.NETWORK/VIRTUALHUBS/DELETE
  - MICROSOFT.NETWORK/VIRTUALHUBS/WRITE
  - MICROSOFT.NETWORK/VIRTUALROUTERS/WRITE
  - MICROSOFT.NETWORK/VIRTUALROUTERS/DELETE
condition: selection
```

## False Positives

- Virtual Network Device being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Virtual Network Device modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_virtual_device_modified_or_deleted.yml)
