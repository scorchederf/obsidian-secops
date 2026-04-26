---
sigma_id: "e3393cba-31f0-4207-831e-aef90ab17a8c"
title: "SAML Token Issuer Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_token_issuer_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_token_issuer_anomaly.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "e3393cba-31f0-4207-831e-aef90ab17a8c"
  - "SAML Token Issuer Anomaly"
attack_technique_ids:
  - "T1606"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SAML Token Issuer Anomaly

Indicates the SAML token issuer for the associated SAML token is potentially compromised. The claims included in the token are unusual or match known attacker patterns

## Metadata

- Rule ID: e3393cba-31f0-4207-831e-aef90ab17a8c
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_token_issuer_anomaly.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1606-forge_web_credentials|T1606]]

## Detection

```yaml
selection:
  riskEventType: tokenIssuerAnomaly
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#token-issuer-anomaly
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_token_issuer_anomaly.yml)
