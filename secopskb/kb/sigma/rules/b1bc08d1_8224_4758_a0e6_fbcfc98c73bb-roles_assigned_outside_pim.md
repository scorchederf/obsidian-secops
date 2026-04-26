---
sigma_id: "b1bc08d1-8224-4758-a0e6-fbcfc98c73bb"
title: "Roles Assigned Outside PIM"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/privileged_identity_management/azure_pim_role_assigned_outside_of_pim.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_assigned_outside_of_pim.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "azure / pim"
aliases:
  - "b1bc08d1-8224-4758-a0e6-fbcfc98c73bb"
  - "Roles Assigned Outside PIM"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Roles Assigned Outside PIM

Identifies when a privilege role assignment has taken place outside of PIM and may indicate an attack.

## Metadata

- Rule ID: b1bc08d1-8224-4758-a0e6-fbcfc98c73bb
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Gloria Lee, '@gleeiamglo'
- Date: 2023-09-14
- Source Path: rules/cloud/azure/privileged_identity_management/azure_pim_role_assigned_outside_of_pim.yml

## Logsource

- product: azure
- service: pim

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  riskEventType: rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
condition: selection
```

## False Positives

- Investigate where users are being assigned privileged roles outside of Privileged Identity Management and prohibit future assignments from there.

## References

- https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-configure-security-alerts#roles-are-being-assigned-outside-of-privileged-identity-management

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/privileged_identity_management/azure_pim_role_assigned_outside_of_pim.yml)
