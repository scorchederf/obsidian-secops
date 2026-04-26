---
sigma_id: "e40f4962-b02b-4192-9bfe-245f7ece1f99"
title: "Multifactor Authentication Denied"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_mfa_denies.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_mfa_denies.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "e40f4962-b02b-4192-9bfe-245f7ece1f99"
  - "Multifactor Authentication Denied"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
  - "T1621"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Multifactor Authentication Denied

User has indicated they haven't instigated the MFA prompt and could indicate an attacker has the password for the account.

## Metadata

- Rule ID: e40f4962-b02b-4192-9bfe-245f7ece1f99
- Status: test
- Level: medium
- Author: AlertIQ
- Date: 2022-03-24
- Source Path: rules/cloud/azure/signin_logs/azure_mfa_denies.yml

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
selection:
  AuthenticationRequirement: multiFactorAuthentication
  Status|contains: MFA Denied
condition: selection
```

## False Positives

- Users actually login but miss-click into the Deny button when MFA prompt.

## References

- https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_mfa_denies.yml)
