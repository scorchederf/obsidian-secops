---
sigma_id: "6c220477-0b5b-4b25-bb90-66183b4089e8"
title: "Suspicious Inbox Forwarding"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_susp_inbox_forwarding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_susp_inbox_forwarding.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "m365 / threat_management"
aliases:
  - "6c220477-0b5b-4b25-bb90-66183b4089e8"
  - "Suspicious Inbox Forwarding"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Inbox Forwarding

Detects when a Microsoft Cloud App Security reported suspicious email forwarding rules, for example, if a user created an inbox rule that forwards a copy of all emails to an external address.

## Metadata

- Rule ID: 6c220477-0b5b-4b25-bb90-66183b4089e8
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-08-22
- Modified: 2022-10-09
- Source Path: rules/cloud/m365/threat_management/microsoft365_susp_inbox_forwarding.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: Suspicious inbox forwarding
  status: success
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-cloud-apps/anomaly-detection-policy
- https://learn.microsoft.com/en-us/defender-cloud-apps/policy-template-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_susp_inbox_forwarding.yml)
