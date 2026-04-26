---
sigma_id: "8dee7a0d-43fd-4b3c-8cd1-605e189d195e"
title: "User State Changed From Guest To Member"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_guest_to_member.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_guest_to_member.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "8dee7a0d-43fd-4b3c-8cd1-605e189d195e"
  - "User State Changed From Guest To Member"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User State Changed From Guest To Member

Detects the change of user type from "Guest" to "Member" for potential elevation of privilege.

## Metadata

- Rule ID: 8dee7a0d-43fd-4b3c-8cd1-605e189d195e
- Status: test
- Level: medium
- Author: MikeDuddington, '@dudders1'
- Date: 2022-06-30
- Source Path: rules/cloud/azure/audit_logs/azure_guest_to_member.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  Category: UserManagement
  OperationName: Update user
  properties.message: '"displayName":"UserType","oldValue":"[\"Guest\"]","newValue":"[\"Member\"]"'
condition: selection
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts#monitoring-external-user-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_guest_to_member.yml)
