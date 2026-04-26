---
sigma_id: "b2572bf9-e20a-4594-b528-40bde666525a"
title: "Impossible Travel"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_impossible_travel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_impossible_travel.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "b2572bf9-e20a-4594-b528-40bde666525a"
  - "Impossible Travel"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Impossible Travel

Identifies user activities originating from geographically distant locations within a time period shorter than the time it takes to travel from the first location to the second.

## Metadata

- Rule ID: b2572bf9-e20a-4594-b528-40bde666525a
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_impossible_travel.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: impossibleTravel
condition: selection
```

## False Positives

- Connecting to a VPN, performing activity and then dropping and performing additional activity.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#impossible-travel
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_impossible_travel.yml)
