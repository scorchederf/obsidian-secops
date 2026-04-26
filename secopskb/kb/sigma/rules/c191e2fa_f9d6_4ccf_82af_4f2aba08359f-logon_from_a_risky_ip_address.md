---
sigma_id: "c191e2fa-f9d6-4ccf-82af-4f2aba08359f"
title: "Logon from a Risky IP Address"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_logon_from_risky_ip_address.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_logon_from_risky_ip_address.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "c191e2fa-f9d6-4ccf-82af-4f2aba08359f"
  - "Logon from a Risky IP Address"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Logon from a Risky IP Address

Detects when a Microsoft Cloud App Security reported when a user signs into your sanctioned apps from a risky IP address.

## Metadata

- Rule ID: c191e2fa-f9d6-4ccf-82af-4f2aba08359f
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_logon_from_risky_ip_address.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Log on from a risky IP address
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_logon_from_risky_ip_address.yml)
