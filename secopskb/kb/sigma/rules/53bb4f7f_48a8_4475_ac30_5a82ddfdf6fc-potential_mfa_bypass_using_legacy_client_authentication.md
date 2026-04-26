---
sigma_id: "53bb4f7f-48a8-4475-ac30-5a82ddfdf6fc"
title: "Potential MFA Bypass Using Legacy Client Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_suspicious_signin_bypassing_mfa.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_suspicious_signin_bypassing_mfa.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "53bb4f7f-48a8-4475-ac30-5a82ddfdf6fc"
  - "Potential MFA Bypass Using Legacy Client Authentication"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential MFA Bypass Using Legacy Client Authentication

Detects successful authentication from potential clients using legacy authentication via user agent strings. This could be a sign of MFA bypass using a password spray attack.

## Metadata

- Rule ID: 53bb4f7f-48a8-4475-ac30-5a82ddfdf6fc
- Status: test
- Level: high
- Author: Harjot Singh, '@cyb3rjy0t'
- Date: 2023-03-20
- Source Path: rules/cloud/azure/signin_logs/azure_ad_suspicious_signin_bypassing_mfa.yml

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
  userAgent|contains:
  - BAV2ROPC
  - CBAinPROD
  - CBAinTAR
condition: selection
```

## False Positives

- Known Legacy Accounts

## References

- https://web.archive.org/web/20230217071802/https://blooteem.com/march-2022
- https://www.microsoft.com/en-us/security/blog/2021/10/26/protect-your-business-from-password-sprays-with-microsoft-dart-recommendations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_suspicious_signin_bypassing_mfa.yml)
