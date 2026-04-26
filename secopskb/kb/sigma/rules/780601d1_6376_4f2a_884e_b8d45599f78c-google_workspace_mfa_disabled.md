---
sigma_id: "780601d1-6376-4f2a-884e-b8d45599f78c"
title: "Google Workspace MFA Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_mfa_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_mfa_disabled.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "780601d1-6376-4f2a-884e-b8d45599f78c"
  - "Google Workspace MFA Disabled"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace MFA Disabled

Detects when multi-factor authentication (MFA) is disabled.

## Metadata

- Rule ID: 780601d1-6376-4f2a-884e-b8d45599f78c
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-26
- Modified: 2023-10-11
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_mfa_disabled.yml

## Logsource

- product: gcp
- service: google_workspace.admin

## Detection

```yaml
selection_base:
  eventService: admin.googleapis.com
  eventName:
  - ENFORCE_STRONG_AUTHENTICATION
  - ALLOW_STRONG_AUTHENTICATION
selection_eventValue:
  new_value: 'false'
condition: all of selection*
```

## False Positives

- MFA may be disabled and performed by a system administrator.

## References

- https://cloud.google.com/logging/docs/audit/gsuite-audit-logging#3
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-security-settings#ENFORCE_STRONG_AUTHENTICATION
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-security-settings?hl=en#ALLOW_STRONG_AUTHENTICATION

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_mfa_disabled.yml)
