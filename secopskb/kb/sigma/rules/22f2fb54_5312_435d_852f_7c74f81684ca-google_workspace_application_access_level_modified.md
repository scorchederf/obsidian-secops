---
sigma_id: "22f2fb54-5312-435d-852f-7c74f81684ca"
title: "Google Workspace Application Access Level Modified"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/gworkspace/gcp_gworkspace_application_access_levels_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_application_access_levels_modified.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / google_workspace.admin"
aliases:
  - "22f2fb54-5312-435d-852f-7c74f81684ca"
  - "Google Workspace Application Access Level Modified"
attack_technique_ids:
  - "T1098.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Workspace Application Access Level Modified

Detects when an access level is changed for a Google workspace application.
An access level is part of BeyondCorp Enterprise which is Google Workspace's way of enforcing Zero Trust model.
An adversary would be able to remove access levels to gain easier access to Google workspace resources.

## Metadata

- Rule ID: 22f2fb54-5312-435d-852f-7c74f81684ca
- Status: test
- Level: medium
- Author: Bryan Lim
- Date: 2024-01-12
- Source Path: rules/cloud/gcp/gworkspace/gcp_gworkspace_application_access_levels_modified.yml

## Logsource

- product: gcp
- service: google_workspace.admin

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]

## Detection

```yaml
selection:
  eventService: admin.googleapis.com
  eventName: CHANGE_APPLICATION_SETTING
  setting_name|startswith: ContextAwareAccess
condition: selection
```

## False Positives

- Legitimate administrative activities changing the access levels for an application

## References

- https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-application-settings
- https://support.google.com/a/answer/9261439

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/gworkspace/gcp_gworkspace_application_access_levels_modified.yml)
