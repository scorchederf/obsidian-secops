---
sigma_id: "128faeef-79dd-44ca-b43c-a9e236a60f49"
title: "Unfamiliar Sign-In Properties"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_unfamilar_sign_in.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_unfamilar_sign_in.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "128faeef-79dd-44ca-b43c-a9e236a60f49"
  - "Unfamiliar Sign-In Properties"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Unfamiliar Sign-In Properties

Detects sign-in with properties that are unfamiliar to the user. The detection considers past sign-in history to look for anomalous sign-ins.

## Metadata

- Rule ID: 128faeef-79dd-44ca-b43c-a9e236a60f49
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_unfamilar_sign_in.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: unfamiliarFeatures
condition: selection
```

## False Positives

- User changing to a new device, location, browser, etc.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#unfamiliar-sign-in-properties
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_unfamilar_sign_in.yml)
