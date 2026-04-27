---
sigma_id: "34d81081-03c9-4a7f-91c9-5e46af625cde"
title: "Bitbucket Unauthorized Full Data Export Triggered"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_unauthorized_full_data_export_triggered.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_unauthorized_full_data_export_triggered.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "critical"
logsource: "bitbucket / audit"
aliases:
  - "34d81081-03c9-4a7f-91c9-5e46af625cde"
  - "Bitbucket Unauthorized Full Data Export Triggered"
attack_technique_ids:
  - "T1213.003"
  - "T1586"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when full data export is attempted an unauthorized user.

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
- [[kb/attack/techniques/T1586-compromise_accounts|T1586: Compromise Accounts]]

## Detection

```yaml
selection:
  auditType.category: Data pipeline
  auditType.action: Unauthorized full data export triggered
condition: selection
```

## False Positives

- Unlikely

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/bitbucketserver/secret-scanning-1157471613.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_unauthorized_full_data_export_triggered.yml)
