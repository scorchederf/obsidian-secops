---
sigma_id: "67d5f8fc-8325-44e4-8f5f-7c0ac07cb5ae"
title: "Measurable Increase Of Successful Authentications"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_auth_sucess_increase.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_sucess_increase.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "azure / signinlogs"
aliases:
  - "67d5f8fc-8325-44e4-8f5f-7c0ac07cb5ae"
  - "Measurable Increase Of Successful Authentications"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Measurable Increase Of Successful Authentications

Detects when successful sign-ins increased by 10% or greater.

## Metadata

- Rule ID: 67d5f8fc-8325-44e4-8f5f-7c0ac07cb5ae
- Status: test
- Level: low
- Author: Mark Morowczynski '@markmorow', MikeDuddington, '@dudders1', Tim Shelton
- Date: 2022-08-11
- Modified: 2022-08-18
- Source Path: rules/cloud/azure/signin_logs/azure_ad_auth_sucess_increase.yml

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
  Count: <10%
condition: selection
```

## False Positives

- Increase of users in the environment

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#monitoring-for-successful-unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_sucess_increase.yml)
