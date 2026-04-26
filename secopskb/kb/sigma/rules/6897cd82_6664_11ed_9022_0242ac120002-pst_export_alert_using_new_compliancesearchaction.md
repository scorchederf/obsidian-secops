---
sigma_id: "6897cd82-6664-11ed-9022-0242ac120002"
title: "PST Export Alert Using New-ComplianceSearchAction"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/threat_management/microsoft365_pst_export_alert_using_new_compliancesearchaction.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_pst_export_alert_using_new_compliancesearchaction.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "m365 / threat_management"
aliases:
  - "6897cd82-6664-11ed-9022-0242ac120002"
  - "PST Export Alert Using New-ComplianceSearchAction"
attack_technique_ids:
  - "T1114"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PST Export Alert Using New-ComplianceSearchAction

Alert when a user has performed an export to a search using 'New-ComplianceSearchAction' with the '-Export' flag. This detection will detect PST export even if the 'eDiscovery search or exported' alert is disabled in the O365.This rule will apply to ExchangePowerShell usage and from the cloud.

## Metadata

- Rule ID: 6897cd82-6664-11ed-9022-0242ac120002
- Status: test
- Level: medium
- Author: Nikita Khalimonenkov
- Date: 2022-11-17
- Source Path: rules/cloud/m365/threat_management/microsoft365_pst_export_alert_using_new_compliancesearchaction.yml

## Logsource

- product: m365
- service: threat_management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1114-email_collection|T1114]]

## Detection

```yaml
selection:
  eventSource: SecurityComplianceCenter
  Payload|contains|all:
  - New-ComplianceSearchAction
  - Export
  - pst
condition: selection
```

## False Positives

- Exporting a PST can be done for legitimate purposes by legitimate sources, but due to the sensitive nature of PST content, it must be monitored.

## References

- https://learn.microsoft.com/en-us/powershell/module/exchange/new-compliancesearchaction?view=exchange-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/threat_management/microsoft365_pst_export_alert_using_new_compliancesearchaction.yml)
