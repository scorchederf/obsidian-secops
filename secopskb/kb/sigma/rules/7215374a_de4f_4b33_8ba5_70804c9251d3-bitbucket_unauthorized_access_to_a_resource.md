---
sigma_id: "7215374a-de4f-4b33-8ba5-70804c9251d3"
title: "Bitbucket Unauthorized Access To A Resource"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_unauthorized_access_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_unauthorized_access_detected.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "critical"
logsource: "bitbucket / audit"
aliases:
  - "7215374a-de4f-4b33-8ba5-70804c9251d3"
  - "Bitbucket Unauthorized Access To A Resource"
attack_technique_ids:
  - "T1586"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bitbucket Unauthorized Access To A Resource

Detects unauthorized access attempts to a resource.

## Metadata

- Rule ID: 7215374a-de4f-4b33-8ba5-70804c9251d3
- Status: test
- Level: critical
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_unauthorized_access_detected.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1586-compromise_accounts|T1586]]

## Detection

```yaml
selection:
  auditType.category: Security
  auditType.action: Unauthorized access to a resource
condition: selection
```

## False Positives

- Access attempts to non-existent repositories or due to outdated plugins. Usually "Anonymous" user is reported in the "author.name" field in most cases.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_unauthorized_access_detected.yml)
