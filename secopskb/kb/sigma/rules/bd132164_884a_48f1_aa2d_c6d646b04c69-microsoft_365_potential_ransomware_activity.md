---
sigma_id: "bd132164-884a-48f1-aa2d-c6d646b04c69"
title: "Microsoft 365 - Potential Ransomware Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_potential_ransomware_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_potential_ransomware_activity.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "bd132164-884a-48f1-aa2d-c6d646b04c69"
  - "Microsoft 365 - Potential Ransomware Activity"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft 365 - Potential Ransomware Activity

Detects when a Microsoft Cloud App Security reported when a user uploads files to the cloud that might be infected with ransomware.

## Metadata

- Rule ID: bd132164-884a-48f1-aa2d-c6d646b04c69
- Status: test
- Level: medium
- Author: austinsonger
- Date: 2021-08-19
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_potential_ransomware_activity.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Potential ransomware activity
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_potential_ransomware_activity.yml)
