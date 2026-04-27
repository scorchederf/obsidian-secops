---
sigma_id: "53acd925-2003-440d-a1f3-71a5253fe237"
title: "Anonymous IP Address"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_address.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_address.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "53acd925-2003-440d-a1f3-71a5253fe237"
  - "Anonymous IP Address"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Indicates sign-ins from an anonymous IP address, for example, using an anonymous browser or VPN.

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528: Steal Application Access Token]]

## Detection

```yaml
selection:
  riskEventType: anonymizedIPAddress
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins

## References

- https://learn.microsoft.com/en-us/graph/api/resources/riskdetection?view=graph-rest-1.0
- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#anonymous-ip-address

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_address.yml)
