---
sigma_id: "ee111937-1fe7-40f0-962a-0eb44d57d174"
title: "Suspicious OAuth App File Download Activities"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_susp_oauth_app_file_download_activities.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_susp_oauth_app_file_download_activities.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "ee111937-1fe7-40f0-962a-0eb44d57d174"
  - "Suspicious OAuth App File Download Activities"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious OAuth App File Download Activities

Detects when a Microsoft Cloud App Security reported when an app downloads multiple files from Microsoft SharePoint or Microsoft OneDrive in a manner that is unusual for the user.

## Metadata

- Rule ID: ee111937-1fe7-40f0-962a-0eb44d57d174
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_susp_oauth_app_file_download_activities.yml

## Logsource

- product: m365
- service: threat_management

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Suspicious OAuth app file download activities
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_susp_oauth_app_file_download_activities.yml)
