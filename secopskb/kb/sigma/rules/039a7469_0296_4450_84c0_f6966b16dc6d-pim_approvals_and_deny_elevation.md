---
sigma_id: "039a7469-0296-4450-84c0-f6966b16dc6d"
title: "PIM Approvals And Deny Elevation"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_pim_activation_approve_deny.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_activation_approve_deny.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "039a7469-0296-4450-84c0-f6966b16dc6d"
  - "PIM Approvals And Deny Elevation"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a PIM elevation is approved or denied. Outside of normal operations should be investigated.

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  properties.message: Request Approved/Denied
condition: selection
```

## False Positives

- Actual admin using PIM.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-identity-management#azure-ad-roles-assignment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_pim_activation_approve_deny.yml)
