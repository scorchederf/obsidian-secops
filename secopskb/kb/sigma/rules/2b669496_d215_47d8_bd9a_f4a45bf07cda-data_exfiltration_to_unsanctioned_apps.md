---
sigma_id: "2b669496-d215-47d8-bd9a-f4a45bf07cda"
title: "Data Exfiltration to Unsanctioned Apps"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_data_exfiltration_to_unsanctioned_app.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_data_exfiltration_to_unsanctioned_app.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "2b669496-d215-47d8-bd9a-f4a45bf07cda"
  - "Data Exfiltration to Unsanctioned Apps"
attack_technique_ids:
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Data Exfiltration to Unsanctioned Apps

Detects when a Microsoft Cloud App Security reported when a user or IP address uses an app that is not sanctioned to perform an activity that resembles an attempt to exfiltrate information from your organization.

## Metadata

- Rule ID: 2b669496-d215-47d8-bd9a-f4a45bf07cda
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_data_exfiltration_to_unsanctioned_app.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1537-transfer_data_to_cloud_account|T1537]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Data exfiltration to unsanctioned apps
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_data_exfiltration_to_unsanctioned_app.yml)
