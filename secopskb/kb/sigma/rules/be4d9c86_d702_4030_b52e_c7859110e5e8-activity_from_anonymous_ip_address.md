---
sigma_id: "be4d9c86-d702-4030-b52e-c7859110e5e8"
title: "Activity From Anonymous IP Address"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_activity.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / riskdetection"
aliases:
  - "be4d9c86-d702-4030-b52e-c7859110e5e8"
  - "Activity From Anonymous IP Address"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Activity From Anonymous IP Address

Identifies that users were active from an IP address that has been identified as an anonymous proxy IP address.

## Metadata

- Rule ID: be4d9c86-d702-4030-b52e-c7859110e5e8
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-03
- Source Path: rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_activity.yml

## Logsource

- product: azure
- service: riskdetection

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: riskyIPAddress
condition: selection
```

## False Positives

- We recommend investigating the sessions flagged by this detection in the context of other sign-ins from the user.

## References

- https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#activity-from-anonymous-ip-address
- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/identity_protection/azure_identity_protection_anonymous_ip_activity.yml)
