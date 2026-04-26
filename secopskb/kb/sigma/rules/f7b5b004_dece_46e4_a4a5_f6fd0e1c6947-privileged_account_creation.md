---
sigma_id: "f7b5b004-dece-46e4-a4a5-f6fd0e1c6947"
title: "Privileged Account Creation"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_privileged_account_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_privileged_account_creation.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "f7b5b004-dece-46e4-a4a5-f6fd0e1c6947"
  - "Privileged Account Creation"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Privileged Account Creation

Detects when a new admin is created.

## Metadata

- Rule ID: f7b5b004-dece-46e4-a4a5-f6fd0e1c6947
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H', Tim Shelton
- Date: 2022-08-11
- Modified: 2022-08-16
- Source Path: rules/cloud/azure/audit_logs/azure_privileged_account_creation.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  properties.message|contains|all:
  - Add user
  - Add member to role
  Status: Success
condition: selection
```

## False Positives

- A legitimate new admin account being created

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts#changes-to-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_privileged_account_creation.yml)
