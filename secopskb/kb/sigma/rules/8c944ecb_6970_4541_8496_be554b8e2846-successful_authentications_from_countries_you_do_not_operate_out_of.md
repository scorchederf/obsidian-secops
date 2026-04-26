---
sigma_id: "8c944ecb-6970-4541-8496-be554b8e2846"
title: "Successful Authentications From Countries You Do Not Operate Out Of"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_authentications_from_countries_you_do_not_operate_out_of.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_authentications_from_countries_you_do_not_operate_out_of.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "8c944ecb-6970-4541-8496-be554b8e2846"
  - "Successful Authentications From Countries You Do Not Operate Out Of"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Successful Authentications From Countries You Do Not Operate Out Of

Detect successful authentications from countries you do not operate out of.

## Metadata

- Rule ID: 8c944ecb-6970-4541-8496-be554b8e2846
- Status: test
- Level: medium
- Author: MikeDuddington, '@dudders1'
- Date: 2022-07-28
- Source Path: rules/cloud/azure/signin_logs/azure_ad_authentications_from_countries_you_do_not_operate_out_of.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  Status: Success
filter:
  Location|contains: <Countries you DO operate out of e,g GB, use OR for multiple>
condition: selection and not filter
```

## False Positives

- If this was approved by System Administrator.

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-user-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_authentications_from_countries_you_do_not_operate_out_of.yml)
