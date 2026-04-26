---
sigma_id: "ff246f56-7f24-402a-baca-b86540e3925c"
title: "Microsoft 365 - User Restricted from Sending Email"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_user_restricted_from_sending_email.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_user_restricted_from_sending_email.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "ff246f56-7f24-402a-baca-b86540e3925c"
  - "Microsoft 365 - User Restricted from Sending Email"
attack_technique_ids:
  - "T1199"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft 365 - User Restricted from Sending Email

Detects when a Security Compliance Center reported a user who exceeded sending limits of the service policies and because of this has been restricted from sending email.

## Metadata

- Rule ID: ff246f56-7f24-402a-baca-b86540e3925c
- Status: test
- Level: medium
- Author: austinsonger
- Date: 2021-08-19
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_user_restricted_from_sending_email.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1199-trusted_relationship|T1199]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: User restricted from sending email
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_user_restricted_from_sending_email.yml)
