---
sigma_id: "0055ad1f-be85-4798-83cf-a6da17c993b3"
title: "Application URI Configuration Changes"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_uri_modifications.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_uri_modifications.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "0055ad1f-be85-4798-83cf-a6da17c993b3"
  - "Application URI Configuration Changes"
attack_technique_ids:
  - "T1528"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a configuration change is made to an applications URI.
URIs for domain names that no longer exist (dangling URIs), not using HTTPS, wildcards at the end of the domain, URIs that are no unique to that app, or URIs that point to domains you do not control should be investigated.

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  properties.message: Update Application Sucess- Property Name AppAddress
condition: selection
```

## False Positives

- When and administrator is making legitimate URI configuration changes to an application. This should be a planned event.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-configuration-changes

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_uri_modifications.yml)
