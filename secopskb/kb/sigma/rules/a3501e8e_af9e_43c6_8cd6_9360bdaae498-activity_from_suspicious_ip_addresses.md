---
sigma_id: "a3501e8e-af9e-43c6-8cd6-9360bdaae498"
title: "Activity from Suspicious IP Addresses"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_detection/microsoft365_from_susp_ip_addresses.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_detection/microsoft365_from_susp_ip_addresses.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "m365 / threat_detection"
aliases:
  - "a3501e8e-af9e-43c6-8cd6-9360bdaae498"
  - "Activity from Suspicious IP Addresses"
attack_technique_ids:
  - "T1573"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Activity from Suspicious IP Addresses

Detects when a Microsoft Cloud App Security reported users were active from an IP address identified as risky by Microsoft Threat Intelligence.
These IP addresses are involved in malicious activities, such as Botnet C&C, and may indicate compromised account.

## Metadata

- Rule ID: a3501e8e-af9e-43c6-8cd6-9360bdaae498
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_detection/microsoft365_from_susp_ip_addresses.yml

## Logsource

- product: m365
- service: threat_detection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1573-encrypted_channel|T1573]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Activity from suspicious IP addresses
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_detection/microsoft365_from_susp_ip_addresses.yml)
