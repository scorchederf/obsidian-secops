---
sigma_id: "28268a8f-191f-4c17-85b2-f5aa4fa829c3"
title: "Google Cloud DNS Zone Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_dns_zone_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_dns_zone_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "28268a8f-191f-4c17-85b2-f5aa4fa829c3"
  - "Google Cloud DNS Zone Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud DNS Zone Modified or Deleted

Identifies when a DNS Zone is modified or deleted in Google Cloud.

## Metadata

- Rule ID: 28268a8f-191f-4c17-85b2-f5aa4fa829c3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-15
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_dns_zone_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - Dns.ManagedZones.Delete
  - Dns.ManagedZones.Update
  - Dns.ManagedZones.Patch
condition: selection
```

## False Positives

- Unknown

## References

- https://cloud.google.com/dns/docs/reference/v1/managedZones

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_dns_zone_modified_or_deleted.yml)
