---
sigma_id: "b831353c-1971-477b-abb6-2828edc3bca1"
title: "Azure Keyvault Secrets Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_keyvault_secrets_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_keyvault_secrets_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "b831353c-1971-477b-abb6-2828edc3bca1"
  - "Azure Keyvault Secrets Modified or Deleted"
attack_technique_ids:
  - "T1552"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Keyvault Secrets Modified or Deleted

Identifies when secrets are modified or deleted in Azure.

## Metadata

- Rule ID: b831353c-1971-477b-abb6-2828edc3bca1
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-16
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_keyvault_secrets_modified_or_deleted.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection:
  operationName:
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/WRITE
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/DELETE
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/BACKUP/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/PURGE/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/UPDATE/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/RECOVER/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/RESTORE/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/SECRETS/SETSECRET/ACTION
condition: selection
```

## False Positives

- Secrets being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Secrets modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_keyvault_secrets_modified_or_deleted.yml)
