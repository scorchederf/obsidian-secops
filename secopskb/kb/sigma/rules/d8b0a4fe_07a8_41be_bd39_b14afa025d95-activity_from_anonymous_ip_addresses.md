---
sigma_id: "d8b0a4fe-07a8-41be-bd39-b14afa025d95"
title: "Activity from Anonymous IP Addresses"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_activity_from_anonymous_ip_addresses.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_from_anonymous_ip_addresses.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "d8b0a4fe-07a8-41be-bd39-b14afa025d95"
  - "Activity from Anonymous IP Addresses"
attack_technique_ids:
  - "T1573"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Activity from Anonymous IP Addresses

Detects when a Microsoft Cloud App Security reported when users were active from an IP address that has been identified as an anonymous proxy IP address.

## Metadata

- Rule ID: d8b0a4fe-07a8-41be-bd39-b14afa025d95
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_activity_from_anonymous_ip_addresses.yml

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
  eventName: Activity from anonymous IP addresses
  status: success
condition: selection
```

## False Positives

- User using a VPN or Proxy

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_activity_from_anonymous_ip_addresses.yml)
