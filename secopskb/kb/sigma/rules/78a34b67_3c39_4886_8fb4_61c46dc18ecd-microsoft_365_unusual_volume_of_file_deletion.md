---
sigma_id: "78a34b67-3c39-4886-8fb4-61c46dc18ecd"
title: "Microsoft 365 - Unusual Volume of File Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_unusual_volume_of_file_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_unusual_volume_of_file_deletion.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "78a34b67-3c39-4886-8fb4-61c46dc18ecd"
  - "Microsoft 365 - Unusual Volume of File Deletion"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft 365 - Unusual Volume of File Deletion

Detects when a Microsoft Cloud App Security reported a user has deleted a unusual a large volume of files.

## Metadata

- Rule ID: 78a34b67-3c39-4886-8fb4-61c46dc18ecd
- Status: test
- Level: medium
- Author: austinsonger
- Date: 2021-08-19
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_unusual_volume_of_file_deletion.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Unusual volume of file deletion
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_unusual_volume_of_file_deletion.yml)
