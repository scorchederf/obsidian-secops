---
sigma_id: "2e669ed8-742e-4fe5-b3c4-5a59b486c2ee"
title: "Activity Performed by Terminated User"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_activity_by_terminated_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_by_terminated_user.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "2e669ed8-742e-4fe5-b3c4-5a59b486c2ee"
  - "Activity Performed by Terminated User"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Activity Performed by Terminated User

Detects when a Microsoft Cloud App Security reported for users whose account were terminated in Azure AD, but still perform activities in other platforms such as AWS or Salesforce.
This is especially relevant for users who use another account to manage resources, since these accounts are often not terminated when a user leaves the company.

## Metadata

- Rule ID: 2e669ed8-742e-4fe5-b3c4-5a59b486c2ee
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_activity_by_terminated_user.yml

## Logsource

- product: m365
- service: threat_management

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Activity performed by terminated user
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_by_terminated_user.yml)
