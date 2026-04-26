---
sigma_id: "4d136857-6a1a-432a-82fc-5dd497ee5e7c"
title: "Sign-ins by Unknown Devices"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_unknown_devices.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_unknown_devices.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "azure / signinlogs"
aliases:
  - "4d136857-6a1a-432a-82fc-5dd497ee5e7c"
  - "Sign-ins by Unknown Devices"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sign-ins by Unknown Devices

Monitor and alert for Sign-ins by unknown devices from non-Trusted locations.

## Metadata

- Rule ID: 4d136857-6a1a-432a-82fc-5dd497ee5e7c
- Status: test
- Level: low
- Author: Michael Epping, '@mepples21'
- Date: 2022-06-28
- Modified: 2022-10-05
- Source Path: rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_unknown_devices.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  AuthenticationRequirement: singleFactorAuthentication
  ResultType: 0
  NetworkLocationDetails: '[]'
  DeviceDetail.deviceId: ''
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#non-compliant-device-sign-in

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_unknown_devices.yml)
