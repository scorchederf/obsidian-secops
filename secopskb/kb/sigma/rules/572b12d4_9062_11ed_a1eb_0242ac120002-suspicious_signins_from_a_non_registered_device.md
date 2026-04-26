---
sigma_id: "572b12d4-9062-11ed-a1eb-0242ac120002"
title: "Suspicious SignIns From A Non Registered Device"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_risky_sign_ins_with_singlefactorauth_from_unknown_devices.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_risky_sign_ins_with_singlefactorauth_from_unknown_devices.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "572b12d4-9062-11ed-a1eb-0242ac120002"
  - "Suspicious SignIns From A Non Registered Device"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious SignIns From A Non Registered Device

Detects risky authentication from a non AD registered device without MFA being required.

## Metadata

- Rule ID: 572b12d4-9062-11ed-a1eb-0242ac120002
- Status: test
- Level: high
- Author: Harjot Singh, '@cyb3rjy0t'
- Date: 2023-01-10
- Modified: 2025-07-02
- Source Path: rules/cloud/azure/signin_logs/azure_ad_risky_sign_ins_with_singlefactorauth_from_unknown_devices.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection_main:
  Status: Success
  AuthenticationRequirement: singleFactorAuthentication
  RiskState: atRisk
selection_empty1:
  DeviceDetail.trusttype: ''
selection_empty2:
  DeviceDetail.trusttype: null
condition: selection_main and 1 of selection_empty*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#non-compliant-device-sign-in

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_risky_sign_ins_with_singlefactorauth_from_unknown_devices.yml)
