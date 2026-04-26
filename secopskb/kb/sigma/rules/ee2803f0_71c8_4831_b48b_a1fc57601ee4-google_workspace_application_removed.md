---
sigma_id: "ee2803f0-71c8-4831-b48b-a1fc57601ee4"
title: "Google Workspace Application Removed"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_application_removed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_application_removed.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "ee2803f0-71c8-4831-b48b-a1fc57601ee4"
  - "Google Workspace Application Removed"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace Application Removed

Detects when an an application is removed from Google Workspace.

## Metadata

- Rule ID: ee2803f0-71c8-4831-b48b-a1fc57601ee4
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-26
- Modified: 2023-10-11
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_application_removed.yml

## Logsource

- product: gcp
- service: google_workspace.admin

## Detection

```yaml
selection:
  eventService: admin.googleapis.com
  eventName:
  - REMOVE_APPLICATION
  - REMOVE_APPLICATION_FROM_WHITELIST
condition: selection
```

## False Positives

- Application being removed may be performed by a System Administrator.

## References

- https://cloud.google.com/logging/docs/audit/gsuite-audit-logging#3
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings?hl=en#REMOVE_APPLICATION
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-domain-settings?hl=en#REMOVE_APPLICATION_FROM_WHITELIST

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_application_removed.yml)
