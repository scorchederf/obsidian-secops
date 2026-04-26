---
sigma_id: "4bb80281-3756-4ec8-a88e-523c5a6fda9e"
title: "New Root Certificate Authority Added"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_new_root_ca_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_new_root_ca_added.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "4bb80281-3756-4ec8-a88e-523c5a6fda9e"
  - "New Root Certificate Authority Added"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Root Certificate Authority Added

Detects newly added root certificate authority to an AzureAD tenant to support certificate based authentication.

## Metadata

- Rule ID: 4bb80281-3756-4ec8-a88e-523c5a6fda9e
- Status: test
- Level: medium
- Author: Harjot Shah Singh, '@cyb3rjy0t'
- Date: 2024-03-26
- Source Path: rules/cloud/azure/audit_logs/azure_ad_new_root_ca_added.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  OperationName: Set Company Information
  TargetResources.modifiedProperties.newValue|contains: TrustedCAsForPasswordlessAuth
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/passwordless-persistence-and-privilege-escalation-in-azure-98a01310be3f
- https://goodworkaround.com/2022/02/15/digging-into-azure-ad-certificate-based-authentication/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_new_root_ca_added.yml)
