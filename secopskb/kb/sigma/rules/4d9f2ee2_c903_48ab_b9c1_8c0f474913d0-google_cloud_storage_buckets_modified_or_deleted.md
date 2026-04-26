---
sigma_id: "4d9f2ee2-c903-48ab-b9c1-8c0f474913d0"
title: "Google Cloud Storage Buckets Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_bucket_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_bucket_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "4d9f2ee2-c903-48ab-b9c1-8c0f474913d0"
  - "Google Cloud Storage Buckets Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Storage Buckets Modified or Deleted

Detects when storage bucket is modified or deleted in Google Cloud.

## Metadata

- Rule ID: 4d9f2ee2-c903-48ab-b9c1-8c0f474913d0
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-14
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_bucket_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - storage.buckets.delete
  - storage.buckets.insert
  - storage.buckets.update
  - storage.buckets.patch
condition: selection
```

## False Positives

- Storage Buckets being modified or deleted may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Storage Buckets modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/storage/docs/json_api/v1/buckets

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_bucket_modified_or_deleted.yml)
