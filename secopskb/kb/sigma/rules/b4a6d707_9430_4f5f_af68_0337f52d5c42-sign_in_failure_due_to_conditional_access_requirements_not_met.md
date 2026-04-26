---
sigma_id: "b4a6d707-9430-4f5f-af68-0337f52d5c42"
title: "Sign-in Failure Due to Conditional Access Requirements Not Met"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_conditional_access_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_conditional_access_failure.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "b4a6d707-9430-4f5f-af68-0337f52d5c42"
  - "Sign-in Failure Due to Conditional Access Requirements Not Met"
attack_technique_ids:
  - "T1110"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sign-in Failure Due to Conditional Access Requirements Not Met

Define a baseline threshold for failed sign-ins due to Conditional Access failures

## Metadata

- Rule ID: b4a6d707-9430-4f5f-af68-0337f52d5c42
- Status: test
- Level: high
- Author: Yochana Henderson, '@Yochana-H'
- Date: 2022-06-01
- Source Path: rules/cloud/azure/signin_logs/azure_conditional_access_failure.yml

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  ResultType: 53003
  Resultdescription: Blocked by Conditional Access
condition: selection
```

## False Positives

- Service Account misconfigured
- Misconfigured Systems
- Vulnerability Scanners

## References

- https://learn.microsoft.com/en-gb/entra/architecture/security-operations-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_conditional_access_failure.yml)
