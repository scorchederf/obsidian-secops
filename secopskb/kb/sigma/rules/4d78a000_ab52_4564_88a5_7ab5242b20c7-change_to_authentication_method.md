---
sigma_id: "4d78a000-ab52-4564-88a5-7ab5242b20c7"
title: "Change to Authentication Method"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_change_to_authentication_method.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_change_to_authentication_method.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "4d78a000-ab52-4564-88a5-7ab5242b20c7"
  - "Change to Authentication Method"
attack_technique_ids:
  - "T1556"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Change to Authentication Method

Change to authentication method could be an indicator of an attacker adding an auth method to the account so they can have continued access.

## Metadata

- Rule ID: 4d78a000-ab52-4564-88a5-7ab5242b20c7
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2021-10-10
- Modified: 2022-12-25
- Source Path: rules/cloud/azure/audit_logs/azure_change_to_authentication_method.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  LoggedByService: Authentication Methods
  Category: UserManagement
  OperationName: User registered security info
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_change_to_authentication_method.yml)
