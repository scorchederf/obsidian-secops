---
sigma_id: "8c6ec464-4ae4-43ac-936a-291da66ed13d"
title: "Roles Are Not Being Used"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_role_not_used.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_not_used.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "8c6ec464-4ae4-43ac-936a-291da66ed13d"
  - "Roles Are Not Being Used"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Roles Are Not Being Used

Identifies when a user has been assigned a privilege role and are not using that role.

## Metadata

- Rule ID: 8c6ec464-4ae4-43ac-936a-291da66ed13d
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-14
- Source Path: rules/cloud/azure/privileged_identity_management/azure_pim_role_not_used.yml

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: redundantAssignmentAlertIncident
condition: selection
```

## False Positives

- Investigate if potential generic account that cannot be removed.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#administrators-arent-using-their-privileged-roles

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_not_used.yml)
