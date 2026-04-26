---
sigma_id: "7091372f-623c-4293-bc37-20c32b3492be"
title: "End User Consent Blocked"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_end_user_consent_blocked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_end_user_consent_blocked.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "7091372f-623c-4293-bc37-20c32b3492be"
  - "End User Consent Blocked"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# End User Consent Blocked

Detects when end user consent is blocked due to risk-based consent.

## Metadata

- Rule ID: 7091372f-623c-4293-bc37-20c32b3492be
- Status: test
- Level: medium
- Author: Bailey Bercik '@baileybercik', Mark Morowczynski '@markmorow'
- Date: 2022-07-10
- Source Path: rules/cloud/azure/audit_logs/azure_app_end_user_consent_blocked.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  failure_status_reason: Microsoft.online.Security.userConsentBlockedForRiskyAppsExceptions
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#end-user-stopped-due-to-risk-based-consent

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_end_user_consent_blocked.yml)
