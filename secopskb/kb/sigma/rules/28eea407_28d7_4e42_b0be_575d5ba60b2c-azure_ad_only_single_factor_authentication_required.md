---
sigma_id: "28eea407-28d7-4e42-b0be-575d5ba60b2c"
title: "Azure AD Only Single Factor Authentication Required"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_only_single_factor_auth_required.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_only_single_factor_auth_required.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "azure / signinlogs"
aliases:
  - "28eea407-28d7-4e42-b0be-575d5ba60b2c"
  - "Azure AD Only Single Factor Authentication Required"
attack_technique_ids:
  - "T1078.004"
  - "T1556.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure AD Only Single Factor Authentication Required

Detect when users are authenticating without MFA being required.

## Metadata

- Rule ID: 28eea407-28d7-4e42-b0be-575d5ba60b2c
- Status: test
- Level: low
- Author: MikeDuddington, '@dudders1'
- Date: 2022-07-27
- Source Path: rules/cloud/azure/signin_logs/azure_ad_only_single_factor_auth_required.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]
- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.006]]

## Detection

```yaml
selection:
  Status: Success
  AuthenticationRequirement: singleFactorAuthentication
condition: selection
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_only_single_factor_auth_required.yml)
