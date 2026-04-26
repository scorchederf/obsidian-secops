---
sigma_id: "99980a85-3a61-43d3-ac0f-b68d6b4797b1"
title: "Google Cloud VPN Tunnel Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_vpn_tunnel_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_vpn_tunnel_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "99980a85-3a61-43d3-ac0f-b68d6b4797b1"
  - "Google Cloud VPN Tunnel Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud VPN Tunnel Modified or Deleted

Identifies when a VPN Tunnel Modified or Deleted in Google Cloud.

## Metadata

- Rule ID: 99980a85-3a61-43d3-ac0f-b68d6b4797b1
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-16
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_vpn_tunnel_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - compute.vpnTunnels.insert
  - compute.vpnTunnels.delete
condition: selection
```

## False Positives

- VPN Tunnel being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- VPN Tunnel modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://any-api.com/googleapis_com/compute/docs/vpnTunnels

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_vpn_tunnel_modified_or_deleted.yml)
