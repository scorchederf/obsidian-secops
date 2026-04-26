---
sigma_id: "6aa12161-235a-4dfb-9c74-fe08df8d8da1"
title: "Bitbucket Audit Log Configuration Updated"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_log_configuration_update_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_log_configuration_update_detected.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "bitbucket / audit"
aliases:
  - "6aa12161-235a-4dfb-9c74-fe08df8d8da1"
  - "Bitbucket Audit Log Configuration Updated"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket Audit Log Configuration Updated

Detects changes to the bitbucket audit log configuration.

## Metadata

- Rule ID: 6aa12161-235a-4dfb-9c74-fe08df8d8da1
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_log_configuration_update_detected.yml

## Logsource

- definition: Requirements: "Basic" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  auditType.category: Auditing
  auditType.action: Audit log configuration updated
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/view-and-configure-the-audit-log-776640417.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_log_configuration_update_detected.yml)
