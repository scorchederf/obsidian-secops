---
sigma_id: "04e2a23a-9b29-4a5c-be3a-3542e3f982ba"
title: "Google Workspace Granted Domain API Access"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_granted_domain_api_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_granted_domain_api_access.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "04e2a23a-9b29-4a5c-be3a-3542e3f982ba"
  - "Google Workspace Granted Domain API Access"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace Granted Domain API Access

Detects when an API access service account is granted domain authority.

## Metadata

- Rule ID: 04e2a23a-9b29-4a5c-be3a-3542e3f982ba
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-23
- Modified: 2023-10-11
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_granted_domain_api_access.yml

## Logsource

- product: gcp
- service: google_workspace.admin

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  eventService: admin.googleapis.com
  eventName: AUTHORIZE_API_CLIENT_ACCESS
condition: selection
```

## False Positives

- Unknown

## References

- https://cloud.google.com/logging/docs/audit/gsuite-audit-logging#3
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings#AUTHORIZE_API_CLIENT_ACCESS

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_granted_domain_api_access.yml)
