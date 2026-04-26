---
sigma_id: "9a60e676-26ac-44c3-814b-0c2a8b977adf"
title: "User Access Blocked by Azure Conditional Access"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_user_login_blocked_by_conditional_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_user_login_blocked_by_conditional_access.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "9a60e676-26ac-44c3-814b-0c2a8b977adf"
  - "User Access Blocked by Azure Conditional Access"
attack_technique_ids:
  - "T1110"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Access Blocked by Azure Conditional Access

Detect access has been blocked by Conditional Access policies.
The access policy does not allow token issuance which might be sights≈ of unauthorizeed login to valid accounts.

## Metadata

- Rule ID: 9a60e676-26ac-44c3-814b-0c2a8b977adf
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2021-10-10
- Modified: 2022-12-25
- Source Path: rules/cloud/azure/signin_logs/azure_user_login_blocked_by_conditional_access.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  ResultType: 53003
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_user_login_blocked_by_conditional_access.yml)
