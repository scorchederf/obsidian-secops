---
sigma_id: "28ecba0a-c743-4690-ad29-9a8f6f25a6f9"
title: "Password Spray Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_password_spray.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_password_spray.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "28ecba0a-c743-4690-ad29-9a8f6f25a6f9"
  - "Password Spray Activity"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Spray Activity

Indicates that a password spray attack has been successfully performed.

## Metadata

- Rule ID: 28ecba0a-c743-4690-ad29-9a8f6f25a6f9
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_password_spray.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  riskEventType: passwordSpray
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#password-spray
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_password_spray.yml)
