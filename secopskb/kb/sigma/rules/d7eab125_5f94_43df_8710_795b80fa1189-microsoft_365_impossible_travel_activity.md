---
sigma_id: "d7eab125-5f94-43df-8710-795b80fa1189"
title: "Microsoft 365 - Impossible Travel Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_impossible_travel_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_impossible_travel_activity.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "d7eab125-5f94-43df-8710-795b80fa1189"
  - "Microsoft 365 - Impossible Travel Activity"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft 365 - Impossible Travel Activity

Detects when a Microsoft Cloud App Security reported a risky sign-in attempt due to a login associated with an impossible travel.

## Metadata

- Rule ID: d7eab125-5f94-43df-8710-795b80fa1189
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2020-07-06
- Modified: 2021-11-27
- Source Path: rules/cloud/m365/threat_management/microsoft365_impossible_travel_activity.yml

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
  eventName: Impossible travel activity
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_impossible_travel_activity.yml)
