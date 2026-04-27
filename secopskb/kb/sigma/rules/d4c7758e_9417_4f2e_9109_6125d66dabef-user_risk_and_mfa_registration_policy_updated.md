---
sigma_id: "d4c7758e-9417-4f2e-9109-6125d66dabef"
title: "User Risk and MFA Registration Policy Updated"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_update_risk_and_mfa_registration_policy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_update_risk_and_mfa_registration_policy.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "d4c7758e-9417-4f2e-9109-6125d66dabef"
  - "User Risk and MFA Registration Policy Updated"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# User Risk and MFA Registration Policy Updated

Detects changes and updates to the user risk and MFA registration policy.
Attackers can modified the policies to Bypass MFA, weaken security thresholds, facilitate further attacks, maintain persistence.

## Metadata

- Rule ID: d4c7758e-9417-4f2e-9109-6125d66dabef
- Status: test
- Level: high
- Author: Harjot Singh (@cyb3rjy0t)
- Date: 2024-08-13
- Source Path: rules/cloud/azure/audit_logs/azure_update_risk_and_mfa_registration_policy.yml

## Logsource

- product: azure
- service: auditlogs

## Detection

```yaml
selection:
  LoggedByService: AAD Management UX
  Category: Policy
  OperationName: Update User Risk and MFA Registration Policy
condition: selection
```

## False Positives

- Known updates by administrators.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-mfa-policy
- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_update_risk_and_mfa_registration_policy.yml)
