---
sigma_id: "5f521e4b-0105-4b72-845b-2198a54487b9"
title: "Users Authenticating To Other Azure AD Tenants"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_users_authenticating_to_other_azure_ad_tenants.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_users_authenticating_to_other_azure_ad_tenants.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "5f521e4b-0105-4b72-845b-2198a54487b9"
  - "Users Authenticating To Other Azure AD Tenants"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Users Authenticating To Other Azure AD Tenants

Detect when users in your Azure AD tenant are authenticating to other Azure AD Tenants.

## Metadata

- Rule ID: 5f521e4b-0105-4b72-845b-2198a54487b9
- Status: test
- Level: medium
- Author: MikeDuddington, '@dudders1'
- Date: 2022-06-30
- Source Path: rules/cloud/azure/signin_logs/azure_users_authenticating_to_other_azure_ad_tenants.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  Status: Success
  HomeTenantId: HomeTenantID
filter:
  ResourceTenantId|contains: HomeTenantID
condition: selection and not filter
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts#monitoring-external-user-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_users_authenticating_to_other_azure_ad_tenants.yml)
