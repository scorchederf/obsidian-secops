---
sigma_id: "6aef64e3-60c6-4782-8db3-8448759c714e"
title: "Google Workspace Role Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_role_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_role_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "6aef64e3-60c6-4782-8db3-8448759c714e"
  - "Google Workspace Role Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace Role Modified or Deleted

Detects when an a role is modified or deleted in Google Workspace.

## Metadata

- Rule ID: 6aef64e3-60c6-4782-8db3-8448759c714e
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-24
- Modified: 2023-10-11
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_role_modified_or_deleted.yml

## Logsource

- product: gcp
- service: google_workspace.admin

## Detection

```yaml
selection:
  eventService: admin.googleapis.com
  eventName:
  - DELETE_ROLE
  - RENAME_ROLE
  - UPDATE_ROLE
condition: selection
```

## False Positives

- Unknown

## References

- https://cloud.google.com/logging/docs/audit/gsuite-audit-logging#3
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-delegated-admin-settings

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_role_modified_or_deleted.yml)
