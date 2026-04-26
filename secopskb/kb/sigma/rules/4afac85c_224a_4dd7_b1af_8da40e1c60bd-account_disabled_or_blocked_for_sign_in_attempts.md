---
sigma_id: "4afac85c-224a-4dd7-b1af-8da40e1c60bd"
title: "Account Disabled or Blocked for Sign in Attempts"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_blocked_account_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_blocked_account_attempt.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "4afac85c-224a-4dd7-b1af-8da40e1c60bd"
  - "Account Disabled or Blocked for Sign in Attempts"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Account Disabled or Blocked for Sign in Attempts

Detects when an account is disabled or blocked for sign in but tried to log in

## Metadata

- Rule ID: 4afac85c-224a-4dd7-b1af-8da40e1c60bd
- Status: test
- Level: medium
- Author: Yochana Henderson, '@Yochana-H'
- Date: 2022-06-17
- Source Path: rules/cloud/azure/signin_logs/azure_blocked_account_attempt.yml

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
  ResultDescription: Failure
condition: selection
```

## False Positives

- Account disabled or blocked in error
- Automation account has been blocked or disabled

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_blocked_account_attempt.yml)
