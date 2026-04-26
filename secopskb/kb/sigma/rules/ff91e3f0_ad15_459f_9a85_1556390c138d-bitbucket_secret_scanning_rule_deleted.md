---
sigma_id: "ff91e3f0-ad15-459f-9a85-1556390c138d"
title: "Bitbucket Secret Scanning Rule Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_rule_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_rule_deleted.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "bitbucket / audit"
aliases:
  - "ff91e3f0-ad15-459f-9a85-1556390c138d"
  - "Bitbucket Secret Scanning Rule Deleted"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket Secret Scanning Rule Deleted

Detects when secret scanning rule is deleted for the project or repository.

## Metadata

- Rule ID: ff91e3f0-ad15-459f-9a85-1556390c138d
- Status: test
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_rule_deleted.yml

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
  auditType.category:
  - Projects
  - Repositories
  auditType.action:
  - Project secret scanning rule deleted
  - Repository secret scanning rule deleted
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/bitbucketserver/secret-scanning-1157471613.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_rule_deleted.yml)
