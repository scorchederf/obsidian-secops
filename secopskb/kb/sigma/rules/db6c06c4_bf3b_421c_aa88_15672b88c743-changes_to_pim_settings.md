---
sigma_id: "db6c06c4-bf3b-421c-aa88-15672b88c743"
title: "Changes To PIM Settings"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_pim_change_settings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_change_settings.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "db6c06c4-bf3b-421c-aa88-15672b88c743"
  - "Changes To PIM Settings"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Changes To PIM Settings

Detects when changes are made to PIM roles

## Metadata

- Rule ID: db6c06c4-bf3b-421c-aa88-15672b88c743
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
- Date: 2022-08-09
- Source Path: rules/cloud/azure/audit_logs/azure_pim_change_settings.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  properties.message: Update role setting in PIM
condition: selection
```

## False Positives

- Legit administrative PIM setting configuration changes

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-identity-management#azure-ad-roles-assignment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_change_settings.yml)
