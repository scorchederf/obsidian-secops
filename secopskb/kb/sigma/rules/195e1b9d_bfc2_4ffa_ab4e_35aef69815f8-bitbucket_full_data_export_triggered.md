---
sigma_id: "195e1b9d-bfc2-4ffa-ab4e-35aef69815f8"
title: "Bitbucket Full Data Export Triggered"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_full_data_export_triggered.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_full_data_export_triggered.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "bitbucket / audit"
aliases:
  - "195e1b9d-bfc2-4ffa-ab4e-35aef69815f8"
  - "Bitbucket Full Data Export Triggered"
attack_technique_ids:
  - "T1213.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bitbucket Full Data Export Triggered

Detects when full data export is attempted.

## Metadata

- Rule ID: 195e1b9d-bfc2-4ffa-ab4e-35aef69815f8
- Status: test
- Level: high
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_full_data_export_triggered.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213.003]]

## Detection

```yaml
selection:
  auditType.category: Data pipeline
  auditType.action: Full data export triggered
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/adminjiraserver0811/importing-and-exporting-data-1019391889.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_full_data_export_triggered.yml)
