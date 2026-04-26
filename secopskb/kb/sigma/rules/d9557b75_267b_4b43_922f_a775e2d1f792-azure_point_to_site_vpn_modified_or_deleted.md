---
sigma_id: "d9557b75-267b-4b43-922f-a775e2d1f792"
title: "Azure Point-to-site VPN Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_network_p2s_vpn_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_p2s_vpn_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "d9557b75-267b-4b43-922f-a775e2d1f792"
  - "Azure Point-to-site VPN Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Point-to-site VPN Modified or Deleted

Identifies when a Point-to-site VPN is Modified or Deleted.

## Metadata

- Rule ID: d9557b75-267b-4b43-922f-a775e2d1f792
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-08
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_network_p2s_vpn_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/WRITE
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/DELETE
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/RESET/ACTION
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/GENERATEVPNPROFILE/ACTION
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/DISCONNECTP2SVPNCONNECTIONS/ACTION
  - MICROSOFT.NETWORK/P2SVPNGATEWAYS/PROVIDERS/MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/WRITE
condition: selection
```

## False Positives

- Point-to-site VPN being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Point-to-site VPN modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_network_p2s_vpn_modified_or_deleted.yml)
