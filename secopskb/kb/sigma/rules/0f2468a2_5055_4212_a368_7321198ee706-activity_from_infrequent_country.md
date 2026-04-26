---
sigma_id: "0f2468a2-5055-4212-a368-7321198ee706"
title: "Activity from Infrequent Country"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_activity_from_infrequent_country.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_from_infrequent_country.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "0f2468a2-5055-4212-a368-7321198ee706"
  - "Activity from Infrequent Country"
attack_technique_ids:
  - "T1573"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Activity from Infrequent Country

Detects when a Microsoft Cloud App Security reported when an activity occurs from a location that wasn't recently or never visited by any user in the organization.

## Metadata

- Rule ID: 0f2468a2-5055-4212-a368-7321198ee706
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_activity_from_infrequent_country.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1573-encrypted_channel|T1573]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Activity from infrequent country
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_from_infrequent_country.yml)
