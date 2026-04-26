---
sigma_id: "5496ff55-42ec-4369-81cb-00f417029e25"
title: "Multifactor Authentication Interrupted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_mfa_interrupted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_mfa_interrupted.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "5496ff55-42ec-4369-81cb-00f417029e25"
  - "Multifactor Authentication Interrupted"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
  - "T1621"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Multifactor Authentication Interrupted

Identifies user login with multifactor authentication failures, which might be an indication an attacker has the password for the account but can't pass the MFA challenge.

## Metadata

- Rule ID: 5496ff55-42ec-4369-81cb-00f417029e25
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2021-10-10
- Modified: 2022-12-18
- Source Path: rules/cloud/azure/signin_logs/azure_mfa_interrupted.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1621-multi-factor_authentication_request_generation|T1621]]

## Detection

```yaml
selection_50074:
  ResultType: 50074
  ResultDescription|contains: Strong Auth required
selection_500121:
  ResultType: 500121
  ResultDescription|contains: Authentication failed during strong authentication request
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_mfa_interrupted.yml)
