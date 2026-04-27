---
sigma_id: "e402c26a-267a-45bd-9615-bd9ceda6da85"
title: "Stale Accounts In A Privileged Role"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_account_stale.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_account_stale.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "e402c26a-267a-45bd-9615-bd9ceda6da85"
  - "Stale Accounts In A Privileged Role"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identifies when an account hasn't signed in during the past n number of days.

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

## Detection

```yaml
selection:
  riskEventType: staleSignInAlertIncident
condition: selection
```

## False Positives

- Investigate if potential generic account that cannot be removed.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#potential-stale-accounts-in-a-privileged-role

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_account_stale.yml)
