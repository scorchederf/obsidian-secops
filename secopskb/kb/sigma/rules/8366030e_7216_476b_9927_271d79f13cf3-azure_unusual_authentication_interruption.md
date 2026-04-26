---
sigma_id: "8366030e-7216-476b-9927-271d79f13cf3"
title: "Azure Unusual Authentication Interruption"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_unusual_authentication_interruption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_unusual_authentication_interruption.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "8366030e-7216-476b-9927-271d79f13cf3"
  - "Azure Unusual Authentication Interruption"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Unusual Authentication Interruption

Detects when there is a interruption in the authentication process.

## Metadata

- Rule ID: 8366030e-7216-476b-9927-271d79f13cf3
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-26
- Modified: 2022-12-18
- Source Path: rules/cloud/azure/signin_logs/azure_unusual_authentication_interruption.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection_50097:
  ResultType: 50097
  ResultDescription: Device authentication is required
selection_50155:
  ResultType: 50155
  ResultDescription: DeviceAuthenticationFailed
selection_50158:
  ResultType: 50158
  ResultDescription: ExternalSecurityChallenge - External security challenge was not
    satisfied
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_unusual_authentication_interruption.yml)
