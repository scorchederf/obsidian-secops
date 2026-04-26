---
sigma_id: "9b2cc4c4-2ad4-416d-8e8e-ee6aa6f5035a"
title: "End User Consent"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_end_user_consent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_end_user_consent.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "azure / auditlogs"
aliases:
  - "9b2cc4c4-2ad4-416d-8e8e-ee6aa6f5035a"
  - "End User Consent"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# End User Consent

Detects when an end user consents to an application

## Metadata

- Rule ID: 9b2cc4c4-2ad4-416d-8e8e-ee6aa6f5035a
- Status: test
- Level: low
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-28
- Source Path: rules/cloud/azure/audit_logs/azure_app_end_user_consent.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  ConsentContext.IsAdminConsent: 'false'
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#end-user-consent

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_end_user_consent.yml)
