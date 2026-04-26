---
sigma_id: "7ea78478-a4f9-42a6-9dcd-f861816122bf"
title: "Disabled MFA to Bypass Authentication Mechanisms"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_mfa_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_mfa_disabled.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "7ea78478-a4f9-42a6-9dcd-f861816122bf"
  - "Disabled MFA to Bypass Authentication Mechanisms"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disabled MFA to Bypass Authentication Mechanisms

Detection for when multi factor authentication has been disabled, which might indicate a malicious activity to bypass authentication mechanisms.

## Metadata

- Rule ID: 7ea78478-a4f9-42a6-9dcd-f861816122bf
- Status: test
- Level: medium
- Author: @ionsor
- Date: 2022-02-08
- Source Path: rules/cloud/azure/activity_logs/azure_mfa_disabled.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  eventSource: AzureActiveDirectory
  eventName: Disable Strong Authentication.
  status: success
condition: selection
```

## False Positives

- Authorized modification by administrators

## References

- https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-userstates

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_mfa_disabled.yml)
