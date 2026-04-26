---
sigma_id: "36440e1c-5c22-467a-889b-593e66498472"
title: "Malicious IP Address Sign-In Suspicious"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address_suspicious.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address_suspicious.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "36440e1c-5c22-467a-889b-593e66498472"
  - "Malicious IP Address Sign-In Suspicious"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious IP Address Sign-In Suspicious

Indicates sign-in from a malicious IP address known to be malicious at time of sign-in.

## Metadata

- Rule ID: 36440e1c-5c22-467a-889b-593e66498472
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-07
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address_suspicious.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  riskEventType: suspiciousIPAddress
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#malicious-ip-address
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address_suspicious.yml)
