---
sigma_id: "4f77e1d7-3982-4ee0-8489-abf2d6b75284"
title: "Sign-ins from Non-Compliant Devices"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_noncompliant_devices.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_noncompliant_devices.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "4f77e1d7-3982-4ee0-8489-abf2d6b75284"
  - "Sign-ins from Non-Compliant Devices"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Monitor and alert for sign-ins where the device was non-compliant.

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  DeviceDetail.isCompliant: 'false'
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#non-compliant-device-sign-in

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_sign_ins_from_noncompliant_devices.yml)
