---
sigma_id: "5259cbf2-0a75-48bf-b57a-c54d6fabaef3"
title: "Bitbucket User Details Export Attempt Detected"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_user_details_export_attempt_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_details_export_attempt_detected.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "bitbucket / audit"
aliases:
  - "5259cbf2-0a75-48bf-b57a-c54d6fabaef3"
  - "Bitbucket User Details Export Attempt Detected"
attack_technique_ids:
  - "T1213"
  - "T1082"
  - "T1591.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket User Details Export Attempt Detected

Detects user data export activity.

## Metadata

- Rule ID: 5259cbf2-0a75-48bf-b57a-c54d6fabaef3
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_user_details_export_attempt_detected.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1591-gather_victim_org_information|T1591.004]]

## Detection

```yaml
selection:
  auditType.category: Users and groups
  auditType.action:
  - User permissions export failed
  - User permissions export started
  - User permissions exported
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://support.atlassian.com/security-and-access-policies/docs/export-user-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_details_export_attempt_detected.yml)
