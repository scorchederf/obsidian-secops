---
sigma_id: "c2496b41-16a9-4016-a776-b23f8910dc58"
title: "Certificate-Based Authentication Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_certificate_based_authencation_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_certificate_based_authencation_enabled.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "c2496b41-16a9-4016-a776-b23f8910dc58"
  - "Certificate-Based Authentication Enabled"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate-Based Authentication Enabled

Detects when certificate based authentication has been enabled in an Azure Active Directory tenant.

## Metadata

- Rule ID: c2496b41-16a9-4016-a776-b23f8910dc58
- Status: test
- Level: medium
- Author: Harjot Shah Singh, '@cyb3rjy0t'
- Date: 2024-03-26
- Source Path: rules/cloud/azure/audit_logs/azure_ad_certificate_based_authencation_enabled.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  OperationName: Authentication Methods Policy Update
  TargetResources.modifiedProperties|contains: AuthenticationMethodsPolicy
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/passwordless-persistence-and-privilege-escalation-in-azure-98a01310be3f
- https://goodworkaround.com/2022/02/15/digging-into-azure-ad-certificate-based-authentication/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_certificate_based_authencation_enabled.yml)
