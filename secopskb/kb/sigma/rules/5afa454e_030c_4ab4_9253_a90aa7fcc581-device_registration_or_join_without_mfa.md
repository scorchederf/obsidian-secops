---
sigma_id: "5afa454e-030c-4ab4-9253-a90aa7fcc581"
title: "Device Registration or Join Without MFA"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_device_registration_or_join_without_mfa.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_device_registration_or_join_without_mfa.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "5afa454e-030c-4ab4-9253-a90aa7fcc581"
  - "Device Registration or Join Without MFA"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Device Registration or Join Without MFA

Monitor and alert for device registration or join events where MFA was not performed.

## Metadata

- Rule ID: 5afa454e-030c-4ab4-9253-a90aa7fcc581
- Status: test
- Level: medium
- Author: Michael Epping, '@mepples21'
- Date: 2022-06-28
- Source Path: rules/cloud/azure/signin_logs/azure_ad_device_registration_or_join_without_mfa.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  ResourceDisplayName: Device Registration Service
  conditionalAccessStatus: success
filter_mfa:
  AuthenticationRequirement: multiFactorAuthentication
condition: selection and not filter_mfa
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#device-registrations-and-joins-outside-policy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_device_registration_or_join_without_mfa.yml)
