---
sigma_id: "f272fb46-25f2-422c-b667-45837994980f"
title: "Authentications To Important Apps Using Single Factor Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_auth_to_important_apps_using_single_factor_auth.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_to_important_apps_using_single_factor_auth.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "f272fb46-25f2-422c-b667-45837994980f"
  - "Authentications To Important Apps Using Single Factor Authentication"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Authentications To Important Apps Using Single Factor Authentication

Detect when authentications to important application(s) only required single-factor authentication

## Metadata

- Rule ID: f272fb46-25f2-422c-b667-45837994980f
- Status: test
- Level: medium
- Author: MikeDuddington, '@dudders1'
- Date: 2022-07-28
- Source Path: rules/cloud/azure/signin_logs/azure_ad_auth_to_important_apps_using_single_factor_auth.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Status: Success
  AppId: Insert Application ID use OR for multiple
  AuthenticationRequirement: singleFactorAuthentication
condition: selection
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_to_important_apps_using_single_factor_auth.yml)
