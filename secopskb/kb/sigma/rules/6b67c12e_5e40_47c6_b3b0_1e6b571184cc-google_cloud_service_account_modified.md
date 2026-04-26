---
sigma_id: "6b67c12e-5e40-47c6-b3b0-1e6b571184cc"
title: "Google Cloud Service Account Modified"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_service_account_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_service_account_modified.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "6b67c12e-5e40-47c6-b3b0-1e6b571184cc"
  - "Google Cloud Service Account Modified"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Service Account Modified

Identifies when a service account is modified in Google Cloud.

## Metadata

- Rule ID: 6b67c12e-5e40-47c6-b3b0-1e6b571184cc
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-14
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_service_account_modified.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name|endswith:
  - .serviceAccounts.patch
  - .serviceAccounts.create
  - .serviceAccounts.update
  - .serviceAccounts.enable
  - .serviceAccounts.undelete
condition: selection
```

## False Positives

- Service Account being modified may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Service Account modified from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_service_account_modified.yml)
