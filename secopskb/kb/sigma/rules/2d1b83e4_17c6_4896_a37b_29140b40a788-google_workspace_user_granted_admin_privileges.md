---
sigma_id: "2d1b83e4-17c6-4896-a37b-29140b40a788"
title: "Google Workspace User Granted Admin Privileges"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_user_granted_admin_privileges.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_user_granted_admin_privileges.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "2d1b83e4-17c6-4896-a37b-29140b40a788"
  - "Google Workspace User Granted Admin Privileges"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace User Granted Admin Privileges

Detects when an Google Workspace user is granted admin privileges.

## Metadata

- Rule ID: 2d1b83e4-17c6-4896-a37b-29140b40a788
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-08-23
- Modified: 2023-10-11
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_user_granted_admin_privileges.yml

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
  eventName:
  - GRANT_DELEGATED_ADMIN_PRIVILEGES
  - GRANT_ADMIN_PRIVILEGE
condition: selection
```

## False Positives

- Google Workspace admin role privileges, may be modified by system administrators.

## References

- https://cloud.google.com/logging/docs/audit/gsuite-audit-logging#3
- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-user-settings#GRANT_ADMIN_PRIVILEGE

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_user_granted_admin_privileges.yml)
