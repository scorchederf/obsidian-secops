---
sigma_id: "19128e5e-4743-48dc-bd97-52e5775af817"
title: "Azure AD Account Credential Leaked"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_leaked_credentials.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_leaked_credentials.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "19128e5e-4743-48dc-bd97-52e5775af817"
  - "Azure AD Account Credential Leaked"
attack_technique_ids:
  - "T1589"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Indicates that the user's valid credentials have been leaked.

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]]

## Detection

```yaml
selection:
  riskEventType: leakedCredentials
condition: selection
```

## False Positives

- A rare hash collision.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#leaked-credentials
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_leaked_credentials.yml)
