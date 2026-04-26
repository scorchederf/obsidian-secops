---
sigma_id: "248649b7-d64f-46f0-9fb2-a52774166fb5"
title: "Application Using Device Code Authentication Flow"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_app_device_code_authentication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_app_device_code_authentication.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "248649b7-d64f-46f0-9fb2-a52774166fb5"
  - "Application Using Device Code Authentication Flow"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Application Using Device Code Authentication Flow

Device code flow is an OAuth 2.0 protocol flow specifically for input constrained devices and is not used in all environments.
If this type of flow is seen in the environment and not being used in an input constrained device scenario, further investigation is warranted.
This can be a misconfigured application or potentially something malicious.

## Metadata

- Rule ID: 248649b7-d64f-46f0-9fb2-a52774166fb5
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
- Date: 2022-06-01
- Source Path: rules/cloud/azure/signin_logs/azure_app_device_code_authentication.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  properties.message: Device Code
condition: selection
```

## False Positives

- Applications that are input constrained will need to use device code flow and are valid authentications.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-authentication-flows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_app_device_code_authentication.yml)
