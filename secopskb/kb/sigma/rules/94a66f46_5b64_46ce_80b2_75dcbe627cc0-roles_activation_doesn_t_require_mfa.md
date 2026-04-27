---
sigma_id: "94a66f46-5b64-46ce-80b2-75dcbe627cc0"
title: "Roles Activation Doesn't Require MFA"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_role_no_mfa_required.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_no_mfa_required.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "94a66f46-5b64-46ce-80b2-75dcbe627cc0"
  - "Roles Activation Doesn't Require MFA"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identifies when a privilege role can be activated without performing mfa.

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

## Detection

```yaml
selection:
  riskEventType: noMfaOnRoleActivationAlertIncident
condition: selection
```

## False Positives

- Investigate if user is performing MFA at sign-in.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#roles-dont-require-multi-factor-authentication-for-activation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_no_mfa_required.yml)
