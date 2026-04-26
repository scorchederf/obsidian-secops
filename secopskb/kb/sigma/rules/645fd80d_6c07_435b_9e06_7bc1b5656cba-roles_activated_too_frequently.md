---
sigma_id: "645fd80d-6c07-435b-9e06-7bc1b5656cba"
title: "Roles Activated Too Frequently"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_role_frequent_activation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_frequent_activation.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "645fd80d-6c07-435b-9e06-7bc1b5656cba"
  - "Roles Activated Too Frequently"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Roles Activated Too Frequently

Identifies when the same privilege role has multiple activations by the same user.

## Metadata

- Rule ID: 645fd80d-6c07-435b-9e06-7bc1b5656cba
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-14
- Source Path: rules/cloud/azure/privileged_identity_management/azure_pim_role_frequent_activation.yml

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: sequentialActivationRenewalsAlertIncident
condition: selection
```

## False Positives

- Investigate where if active time period for a role is set too short.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#roles-are-being-activated-too-frequently

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_frequent_activation.yml)
