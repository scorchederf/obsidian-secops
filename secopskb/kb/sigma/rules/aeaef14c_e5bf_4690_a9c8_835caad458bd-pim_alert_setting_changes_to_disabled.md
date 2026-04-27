---
sigma_id: "aeaef14c-e5bf-4690-a9c8-835caad458bd"
title: "PIM Alert Setting Changes To Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_pim_alerts_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_alerts_disabled.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "aeaef14c-e5bf-4690-a9c8-835caad458bd"
  - "PIM Alert Setting Changes To Disabled"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PIM Alert Setting Changes To Disabled

Detects when PIM alerts are set to disabled.

## Metadata

- Rule ID: aeaef14c-e5bf-4690-a9c8-835caad458bd
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
- Date: 2022-08-09
- Source Path: rules/cloud/azure/audit_logs/azure_pim_alerts_disabled.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  properties.message: Disable PIM Alert
condition: selection
```

## False Positives

- Administrator disabling PIM alerts as an active choice.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-identity-management#azure-ad-roles-assignment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_alerts_disabled.yml)
