---
sigma_id: "a84fc3b1-c9ce-4125-8e74-bdcdb24021f1"
title: "Primary Refresh Token Access Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_prt_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_prt_access.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "a84fc3b1-c9ce-4125-8e74-bdcdb24021f1"
  - "Primary Refresh Token Access Attempt"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Primary Refresh Token Access Attempt

Indicates access attempt to the PRT resource which can be used to move laterally into an organization or perform credential theft

## Metadata

- Rule ID: a84fc3b1-c9ce-4125-8e74-bdcdb24021f1
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-07
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_prt_access.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  riskEventType: attemptedPrtAccess
condition: selection
```

## False Positives

- This detection is low-volume and is seen infrequently in most organizations. When this detection appears it's high risk, and users should be remediated.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#possible-attempt-to-access-primary-refresh-token-prt
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_prt_access.yml)
