---
sigma_id: "55695bc0-c8cf-461f-a379-2535f563c854"
title: "Applications That Are Using ROPC Authentication Flow"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_app_ropc_authentication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_app_ropc_authentication.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / signinlogs"
aliases:
  - "55695bc0-c8cf-461f-a379-2535f563c854"
  - "Applications That Are Using ROPC Authentication Flow"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Applications That Are Using ROPC Authentication Flow

Resource owner password credentials (ROPC) should be avoided if at all possible as this requires the user to expose their current password credentials to the application directly.
The application then uses those credentials to authenticate the user against the identity provider.

## Metadata

- Rule ID: 55695bc0-c8cf-461f-a379-2535f563c854
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
- Date: 2022-06-01
- Source Path: rules/cloud/azure/signin_logs/azure_app_ropc_authentication.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  properties.message: ROPC
condition: selection
```

## False Positives

- Applications that are being used as part of automated testing or a legacy application that cannot use any other modern authentication flow

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-authentication-flows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_app_ropc_authentication.yml)
