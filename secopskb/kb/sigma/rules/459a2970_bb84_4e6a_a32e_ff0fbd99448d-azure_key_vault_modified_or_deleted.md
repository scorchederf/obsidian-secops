---
sigma_id: "459a2970-bb84-4e6a-a32e-ff0fbd99448d"
title: "Azure Key Vault Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_keyvault_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_keyvault_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "459a2970-bb84-4e6a-a32e-ff0fbd99448d"
  - "Azure Key Vault Modified or Deleted"
attack_technique_ids:
  - "T1552"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Key Vault Modified or Deleted

Identifies when a key vault is modified or deleted.

## Metadata

- Rule ID: 459a2970-bb84-4e6a-a32e-ff0fbd99448d
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-16
- Modified: 2022-08-23
- Source Path: rules/cloud/azure/activity_logs/azure_keyvault_modified_or_deleted.yml

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
  - MICROSOFT.KEYVAULT/VAULTS/WRITE
  - MICROSOFT.KEYVAULT/VAULTS/DELETE
  - MICROSOFT.KEYVAULT/VAULTS/DEPLOY/ACTION
  - MICROSOFT.KEYVAULT/VAULTS/ACCESSPOLICIES/WRITE
condition: selection
```

## False Positives

- Key Vault being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Key Vault modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_keyvault_modified_or_deleted.yml)
