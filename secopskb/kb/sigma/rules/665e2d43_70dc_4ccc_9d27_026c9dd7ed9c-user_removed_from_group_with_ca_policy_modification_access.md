---
sigma_id: "665e2d43-70dc-4ccc-9d27-026c9dd7ed9c"
title: "User Removed From Group With CA Policy Modification Access"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_group_user_removal_ca_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_group_user_removal_ca_modification.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "665e2d43-70dc-4ccc-9d27-026c9dd7ed9c"
  - "User Removed From Group With CA Policy Modification Access"
attack_technique_ids:
  - "T1548"
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Removed From Group With CA Policy Modification Access

Monitor and alert on group membership removal of groups that have CA policy modification access

## Metadata

- Rule ID: 665e2d43-70dc-4ccc-9d27-026c9dd7ed9c
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Thomas Detzner '@tdetzner'
- Date: 2022-08-04
- Source Path: rules/cloud/azure/audit_logs/azure_group_user_removal_ca_modification.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]
- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  properties.message: Remove member from group
condition: selection
```

## False Positives

- User removed from the group is approved

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-infrastructure#conditional-access

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_group_user_removal_ca_modification.yml)
