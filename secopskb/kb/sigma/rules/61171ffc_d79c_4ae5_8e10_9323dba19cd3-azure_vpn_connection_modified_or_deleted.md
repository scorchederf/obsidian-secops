---
sigma_id: "61171ffc-d79c-4ae5-8e10-9323dba19cd3"
title: "Azure VPN Connection Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_vpn_connection_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_vpn_connection_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "61171ffc-d79c-4ae5-8e10-9323dba19cd3"
  - "Azure VPN Connection Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure VPN Connection Modified or Deleted

Identifies when a VPN connection is modified or deleted.

## Metadata

- Rule ID: 61171ffc-d79c-4ae5-8e10-9323dba19cd3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_vpn_connection_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/VPNGATEWAYS/VPNCONNECTIONS/WRITE
  - MICROSOFT.NETWORK/VPNGATEWAYS/VPNCONNECTIONS/DELETE
condition: selection
```

## False Positives

- VPN Connection being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- VPN Connection modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_vpn_connection_modified_or_deleted.yml)
