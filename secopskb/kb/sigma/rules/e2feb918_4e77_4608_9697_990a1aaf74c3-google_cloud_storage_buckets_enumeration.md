---
sigma_id: "e2feb918-4e77-4608-9697-990a1aaf74c3"
title: "Google Cloud Storage Buckets Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_bucket_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_bucket_enumeration.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "low"
logsource: "gcp / gcp.audit"
aliases:
  - "e2feb918-4e77-4608-9697-990a1aaf74c3"
  - "Google Cloud Storage Buckets Enumeration"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Storage Buckets Enumeration

Detects when storage bucket is enumerated in Google Cloud.

## Metadata

- Rule ID: e2feb918-4e77-4608-9697-990a1aaf74c3
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-08-14
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_bucket_enumeration.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - storage.buckets.list
  - storage.buckets.listChannels
condition: selection
```

## False Positives

- Storage Buckets being enumerated may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Storage Buckets enumerated from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/storage/docs/json_api/v1/buckets

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_bucket_enumeration.yml)
