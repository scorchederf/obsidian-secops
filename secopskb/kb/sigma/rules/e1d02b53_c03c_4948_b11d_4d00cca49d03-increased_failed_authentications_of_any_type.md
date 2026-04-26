---
sigma_id: "e1d02b53-c03c-4948-b11d-4d00cca49d03"
title: "Increased Failed Authentications Of Any Type"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_auth_failure_increase.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_failure_increase.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "e1d02b53-c03c-4948-b11d-4d00cca49d03"
  - "Increased Failed Authentications Of Any Type"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Increased Failed Authentications Of Any Type

Detects when sign-ins increased by 10% or greater.

## Metadata

- Rule ID: e1d02b53-c03c-4948-b11d-4d00cca49d03
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', MikeDuddington, '@dudders1'
- Date: 2022-08-11
- Source Path: rules/cloud/azure/signin_logs/azure_ad_auth_failure_increase.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Status: failure
  Count: <10%
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#monitoring-for-failed-unusual-sign-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_auth_failure_increase.yml)
