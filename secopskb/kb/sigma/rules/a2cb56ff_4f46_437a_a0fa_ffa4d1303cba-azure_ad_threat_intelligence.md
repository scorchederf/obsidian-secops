---
sigma_id: "a2cb56ff-4f46-437a-a0fa-ffa4d1303cba"
title: "Azure AD Threat Intelligence"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_threat_intel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_threat_intel.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "a2cb56ff-4f46-437a-a0fa-ffa4d1303cba"
  - "Azure AD Threat Intelligence"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Indicates user activity that is unusual for the user or consistent with known attack patterns.

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

## Detection

```yaml
selection:
  riskEventType: investigationsThreatIntelligence
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#azure-ad-threat-intelligence-sign-in
- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#azure-ad-threat-intelligence-user
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_threat_intel.yml)
