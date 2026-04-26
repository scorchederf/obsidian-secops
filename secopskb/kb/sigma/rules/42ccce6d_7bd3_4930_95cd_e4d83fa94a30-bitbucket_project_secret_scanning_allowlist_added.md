---
sigma_id: "42ccce6d-7bd3-4930-95cd-e4d83fa94a30"
title: "Bitbucket Project Secret Scanning Allowlist Added"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_project_secret_scanning_allowlist_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_project_secret_scanning_allowlist_added.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "bitbucket / audit"
aliases:
  - "42ccce6d-7bd3-4930-95cd-e4d83fa94a30"
  - "Bitbucket Project Secret Scanning Allowlist Added"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket Project Secret Scanning Allowlist Added

Detects when a secret scanning allowlist rule is added for projects.

## Metadata

- Rule ID: 42ccce6d-7bd3-4930-95cd-e4d83fa94a30
- Status: test
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_project_secret_scanning_allowlist_added.yml

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
  auditType.category: Projects
  auditType.action: Project secret scanning allowlist rule added
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/bitbucketserver/secret-scanning-1157471613.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_project_secret_scanning_allowlist_added.yml)
