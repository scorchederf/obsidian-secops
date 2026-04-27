---
sigma_id: "258b6593-215d-4a26-a141-c8e31c1299a6"
title: "Anomalous User Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_anomalous_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anomalous_user.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "258b6593-215d-4a26-a141-c8e31c1299a6"
  - "Anomalous User Activity"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Anomalous User Activity

Indicates that there are anomalous patterns of behavior like suspicious changes to the directory.

## Metadata

- Rule ID: 258b6593-215d-4a26-a141-c8e31c1299a6
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_anomalous_user.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  riskEventType: anomalousUserActivity
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#anomalous-user-activity
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anomalous_user.yml)
