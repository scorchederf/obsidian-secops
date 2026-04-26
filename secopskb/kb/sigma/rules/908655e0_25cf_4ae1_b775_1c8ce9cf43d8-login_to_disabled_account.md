---
sigma_id: "908655e0-25cf-4ae1-b775-1c8ce9cf43d8"
title: "Login to Disabled Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_login_to_disabled_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_login_to_disabled_account.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "908655e0-25cf-4ae1-b775-1c8ce9cf43d8"
  - "Login to Disabled Account"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Login to Disabled Account

Detect failed attempts to sign in to disabled accounts.

## Metadata

- Rule ID: 908655e0-25cf-4ae1-b775-1c8ce9cf43d8
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2021-10-10
- Modified: 2022-12-25
- Source Path: rules/cloud/azure/signin_logs/azure_login_to_disabled_account.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  ResultType: 50057
  ResultDescription: User account is disabled. The account has been disabled by an
    administrator.
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_login_to_disabled_account.yml)
