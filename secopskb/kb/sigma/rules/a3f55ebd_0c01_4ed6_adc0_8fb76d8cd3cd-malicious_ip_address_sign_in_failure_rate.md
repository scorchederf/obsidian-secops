---
sigma_id: "a3f55ebd-0c01-4ed6-adc0-8fb76d8cd3cd"
title: "Malicious IP Address Sign-In Failure Rate"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "a3f55ebd-0c01-4ed6-adc0-8fb76d8cd3cd"
  - "Malicious IP Address Sign-In Failure Rate"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious IP Address Sign-In Failure Rate

Indicates sign-in from a malicious IP address based on high failure rates.

## Metadata

- Rule ID: a3f55ebd-0c01-4ed6-adc0-8fb76d8cd3cd
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-07
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  riskEventType: maliciousIPAddress
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#malicious-ip-address
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_malicious_ip_address.yml)
