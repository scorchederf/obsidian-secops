---
sigma_id: "18b88d08-d73e-4f21-bc25-4b9892a4fdd0"
title: "PST Export Alert Using eDiscovery Alert"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_pst_export_alert.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_pst_export_alert.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "18b88d08-d73e-4f21-bc25-4b9892a4fdd0"
  - "PST Export Alert Using eDiscovery Alert"
attack_technique_ids:
  - "T1114"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PST Export Alert Using eDiscovery Alert

Alert on when a user has performed an eDiscovery search or exported a PST file from the search. This PST file usually has sensitive information including email body content

## Metadata

- Rule ID: 18b88d08-d73e-4f21-bc25-4b9892a4fdd0
- Status: test
- Level: medium
- Author: Sorina Ionescu
- Date: 2022-02-08
- Modified: 2022-11-17
- Source Path: rules/cloud/m365/threat_management/microsoft365_pst_export_alert.yml

## Logsource

- definition: Requires the 'eDiscovery search or exported' alert to be enabled
- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1114-email_collection|T1114]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  eventName: eDiscovery search started or exported
  status: success
condition: selection
```

## False Positives

- PST export can be done for legitimate purposes but due to the sensitive nature of its content it must be monitored.

## References

- https://learn.microsoft.com/en-us/microsoft-365/compliance/alert-policies?view=o365-worldwide

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_pst_export_alert.yml)
