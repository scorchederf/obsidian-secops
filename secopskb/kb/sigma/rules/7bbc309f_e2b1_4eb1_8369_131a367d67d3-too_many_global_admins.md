---
sigma_id: "7bbc309f-e2b1-4eb1-8369-131a367d67d3"
title: "Too Many Global Admins"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_too_many_global_admins.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_too_many_global_admins.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "7bbc309f-e2b1-4eb1-8369-131a367d67d3"
  - "Too Many Global Admins"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Too Many Global Admins

Identifies an event where there are there are too many accounts assigned the Global Administrator role.

## Metadata

- Rule ID: 7bbc309f-e2b1-4eb1-8369-131a367d67d3
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-14
- Source Path: rules/cloud/azure/privileged_identity_management/azure_pim_too_many_global_admins.yml

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: tooManyGlobalAdminsAssignedToTenantAlertIncident
condition: selection
```

## False Positives

- Investigate if threshold setting in PIM is too low.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#there-are-too-many-global-administrators

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_too_many_global_admins.yml)
