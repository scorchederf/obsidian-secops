---
sigma_id: "2b7d6fc0-71ac-4cf7-8ed1-b5788ee5257a"
title: "Account Lockout"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_account_lockout.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_account_lockout.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "2b7d6fc0-71ac-4cf7-8ed1-b5788ee5257a"
  - "Account Lockout"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Account Lockout

Identifies user account which has been locked because the user tried to sign in too many times with an incorrect user ID or password.

## Metadata

- Rule ID: 2b7d6fc0-71ac-4cf7-8ed1-b5788ee5257a
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2021-10-10
- Modified: 2022-12-25
- Source Path: rules/cloud/azure/signin_logs/azure_account_lockout.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  ResultType: 50053
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_account_lockout.yml)
